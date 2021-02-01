import ipaddress
import wgconfig
from modules.DB import db, Settings, Profile
from modules.wgtools.wgtools import keypair
from app import app
wg = wgconfig.WGConfig(app.config['WIREGUARD_CONFIG_FILE'])

class VPN:

	# Generate keypair for the server
	def generate_server_keys():
		if Settings.query.filter_by(key='server_private_key').first() is None:
			private_key, public_key = keypair()
			private_key_setting = Settings(key='server_private_key', value=private_key)
			public_key_setting = Settings(key='server_public_key', value=public_key)
			db.session.add_all(instances=[private_key_setting, public_key_setting])
			db.session.commit()
			return True
		else:
			return False

	# Generate keypair for a profile
	def generate_profile_keys():
		print(Settings.query.with_entities(Settings.key).all())
		return keypair()

	# Add peer to Wireguard
	def add_peer(user_uuid, name, public_key):
		try:
			# Check if the peer already exists
			wg.read_file()
			if wg.peers[public_key] is not None:
				return False
			else:
				# We need to assign an IP to this peer, let's pick a free IP
				reserved_ips = []
				for ip in Profile.query.with_entities(Profile.ip_address).all():
					reserved_ips.append(ip[0])
				possible_ips = []
				for ip in ipaddress.IPv4Network(app.config['VPN_NETWORK']):
					possible_ips.append(str(ip))
				selected_ip = list(set(reserved_ips).symmetric_difference(set(possible_ips)))[0]
				wg.add_peer(public_key, leading_comment=f'# {user_uuid} - {name}')
				wg.add_attr(public_key, 'AllowedIPs', f'{selected_ip}/32')
				wg.write_file()
		except Exception:
			return False