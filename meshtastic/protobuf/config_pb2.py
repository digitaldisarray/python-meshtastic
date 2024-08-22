# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/protobuf/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n meshtastic/protobuf/config.proto\x12\x13meshtastic.protobuf\"\xdc#\n\x06\x43onfig\x12:\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32(.meshtastic.protobuf.Config.DeviceConfigH\x00\x12>\n\x08position\x18\x02 \x01(\x0b\x32*.meshtastic.protobuf.Config.PositionConfigH\x00\x12\x38\n\x05power\x18\x03 \x01(\x0b\x32\'.meshtastic.protobuf.Config.PowerConfigH\x00\x12<\n\x07network\x18\x04 \x01(\x0b\x32).meshtastic.protobuf.Config.NetworkConfigH\x00\x12<\n\x07\x64isplay\x18\x05 \x01(\x0b\x32).meshtastic.protobuf.Config.DisplayConfigH\x00\x12\x36\n\x04lora\x18\x06 \x01(\x0b\x32&.meshtastic.protobuf.Config.LoRaConfigH\x00\x12@\n\tbluetooth\x18\x07 \x01(\x0b\x32+.meshtastic.protobuf.Config.BluetoothConfigH\x00\x1a\xa7\x05\n\x0c\x44\x65viceConfig\x12;\n\x04role\x18\x01 \x01(\x0e\x32-.meshtastic.protobuf.Config.DeviceConfig.Role\x12\x16\n\x0eserial_enabled\x18\x02 \x01(\x08\x12\x19\n\x11\x64\x65\x62ug_log_enabled\x18\x03 \x01(\x08\x12\x13\n\x0b\x62utton_gpio\x18\x04 \x01(\r\x12\x13\n\x0b\x62uzzer_gpio\x18\x05 \x01(\r\x12R\n\x10rebroadcast_mode\x18\x06 \x01(\x0e\x32\x38.meshtastic.protobuf.Config.DeviceConfig.RebroadcastMode\x12 \n\x18node_info_broadcast_secs\x18\x07 \x01(\r\x12\"\n\x1a\x64ouble_tap_as_button_press\x18\x08 \x01(\x08\x12\x12\n\nis_managed\x18\t \x01(\x08\x12\x1c\n\x14\x64isable_triple_click\x18\n \x01(\x08\x12\r\n\x05tzdef\x18\x0b \x01(\t\x12\x1e\n\x16led_heartbeat_disabled\x18\x0c \x01(\x08\"\xae\x01\n\x04Role\x12\n\n\x06\x43LIENT\x10\x00\x12\x0f\n\x0b\x43LIENT_MUTE\x10\x01\x12\n\n\x06ROUTER\x10\x02\x12\x15\n\rROUTER_CLIENT\x10\x03\x1a\x02\x08\x01\x12\x0c\n\x08REPEATER\x10\x04\x12\x0b\n\x07TRACKER\x10\x05\x12\n\n\x06SENSOR\x10\x06\x12\x07\n\x03TAK\x10\x07\x12\x11\n\rCLIENT_HIDDEN\x10\x08\x12\x12\n\x0eLOST_AND_FOUND\x10\t\x12\x0f\n\x0bTAK_TRACKER\x10\n\"Q\n\x0fRebroadcastMode\x12\x07\n\x03\x41LL\x10\x00\x12\x15\n\x11\x41LL_SKIP_DECODING\x10\x01\x12\x0e\n\nLOCAL_ONLY\x10\x02\x12\x0e\n\nKNOWN_ONLY\x10\x03\x1a\x9a\x05\n\x0ePositionConfig\x12\x1f\n\x17position_broadcast_secs\x18\x01 \x01(\r\x12(\n position_broadcast_smart_enabled\x18\x02 \x01(\x08\x12\x16\n\x0e\x66ixed_position\x18\x03 \x01(\x08\x12\x17\n\x0bgps_enabled\x18\x04 \x01(\x08\x42\x02\x18\x01\x12\x1b\n\x13gps_update_interval\x18\x05 \x01(\r\x12\x1c\n\x10gps_attempt_time\x18\x06 \x01(\rB\x02\x18\x01\x12\x16\n\x0eposition_flags\x18\x07 \x01(\r\x12\x0f\n\x07rx_gpio\x18\x08 \x01(\r\x12\x0f\n\x07tx_gpio\x18\t \x01(\r\x12(\n broadcast_smart_minimum_distance\x18\n \x01(\r\x12-\n%broadcast_smart_minimum_interval_secs\x18\x0b \x01(\r\x12\x13\n\x0bgps_en_gpio\x18\x0c \x01(\r\x12\x44\n\x08gps_mode\x18\r \x01(\x0e\x32\x32.meshtastic.protobuf.Config.PositionConfig.GpsMode\"\xab\x01\n\rPositionFlags\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x41LTITUDE\x10\x01\x12\x10\n\x0c\x41LTITUDE_MSL\x10\x02\x12\x16\n\x12GEOIDAL_SEPARATION\x10\x04\x12\x07\n\x03\x44OP\x10\x08\x12\t\n\x05HVDOP\x10\x10\x12\r\n\tSATINVIEW\x10 \x12\n\n\x06SEQ_NO\x10@\x12\x0e\n\tTIMESTAMP\x10\x80\x01\x12\x0c\n\x07HEADING\x10\x80\x02\x12\n\n\x05SPEED\x10\x80\x04\"5\n\x07GpsMode\x12\x0c\n\x08\x44ISABLED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0f\n\x0bNOT_PRESENT\x10\x02\x1a\x84\x02\n\x0bPowerConfig\x12\x17\n\x0fis_power_saving\x18\x01 \x01(\x08\x12&\n\x1eon_battery_shutdown_after_secs\x18\x02 \x01(\r\x12\x1f\n\x17\x61\x64\x63_multiplier_override\x18\x03 \x01(\x02\x12\x1b\n\x13wait_bluetooth_secs\x18\x04 \x01(\r\x12\x10\n\x08sds_secs\x18\x06 \x01(\r\x12\x0f\n\x07ls_secs\x18\x07 \x01(\r\x12\x15\n\rmin_wake_secs\x18\x08 \x01(\r\x12\"\n\x1a\x64\x65vice_battery_ina_address\x18\t \x01(\r\x12\x18\n\x10powermon_enables\x18  \x01(\x04\x1a\x90\x03\n\rNetworkConfig\x12\x14\n\x0cwifi_enabled\x18\x01 \x01(\x08\x12\x11\n\twifi_ssid\x18\x03 \x01(\t\x12\x10\n\x08wifi_psk\x18\x04 \x01(\t\x12\x12\n\nntp_server\x18\x05 \x01(\t\x12\x13\n\x0b\x65th_enabled\x18\x06 \x01(\x08\x12K\n\x0c\x61\x64\x64ress_mode\x18\x07 \x01(\x0e\x32\x35.meshtastic.protobuf.Config.NetworkConfig.AddressMode\x12I\n\x0bipv4_config\x18\x08 \x01(\x0b\x32\x34.meshtastic.protobuf.Config.NetworkConfig.IpV4Config\x12\x16\n\x0ersyslog_server\x18\t \x01(\t\x1a\x46\n\nIpV4Config\x12\n\n\x02ip\x18\x01 \x01(\x07\x12\x0f\n\x07gateway\x18\x02 \x01(\x07\x12\x0e\n\x06subnet\x18\x03 \x01(\x07\x12\x0b\n\x03\x64ns\x18\x04 \x01(\x07\"#\n\x0b\x41\x64\x64ressMode\x12\x08\n\x04\x44HCP\x10\x00\x12\n\n\x06STATIC\x10\x01\x1a\xfa\x07\n\rDisplayConfig\x12\x16\n\x0escreen_on_secs\x18\x01 \x01(\r\x12Q\n\ngps_format\x18\x02 \x01(\x0e\x32=.meshtastic.protobuf.Config.DisplayConfig.GpsCoordinateFormat\x12!\n\x19\x61uto_screen_carousel_secs\x18\x03 \x01(\r\x12\x19\n\x11\x63ompass_north_top\x18\x04 \x01(\x08\x12\x13\n\x0b\x66lip_screen\x18\x05 \x01(\x08\x12\x45\n\x05units\x18\x06 \x01(\x0e\x32\x36.meshtastic.protobuf.Config.DisplayConfig.DisplayUnits\x12@\n\x04oled\x18\x07 \x01(\x0e\x32\x32.meshtastic.protobuf.Config.DisplayConfig.OledType\x12J\n\x0b\x64isplaymode\x18\x08 \x01(\x0e\x32\x35.meshtastic.protobuf.Config.DisplayConfig.DisplayMode\x12\x14\n\x0cheading_bold\x18\t \x01(\x08\x12\x1d\n\x15wake_on_tap_or_motion\x18\n \x01(\x08\x12Y\n\x13\x63ompass_orientation\x18\x0b \x01(\x0e\x32<.meshtastic.protobuf.Config.DisplayConfig.CompassOrientation\"M\n\x13GpsCoordinateFormat\x12\x07\n\x03\x44\x45\x43\x10\x00\x12\x07\n\x03\x44MS\x10\x01\x12\x07\n\x03UTM\x10\x02\x12\x08\n\x04MGRS\x10\x03\x12\x07\n\x03OLC\x10\x04\x12\x08\n\x04OSGR\x10\x05\"(\n\x0c\x44isplayUnits\x12\n\n\x06METRIC\x10\x00\x12\x0c\n\x08IMPERIAL\x10\x01\"M\n\x08OledType\x12\r\n\tOLED_AUTO\x10\x00\x12\x10\n\x0cOLED_SSD1306\x10\x01\x12\x0f\n\x0bOLED_SH1106\x10\x02\x12\x0f\n\x0bOLED_SH1107\x10\x03\"A\n\x0b\x44isplayMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08TWOCOLOR\x10\x01\x12\x0c\n\x08INVERTED\x10\x02\x12\t\n\x05\x43OLOR\x10\x03\"\xba\x01\n\x12\x43ompassOrientation\x12\r\n\tDEGREES_0\x10\x00\x12\x0e\n\nDEGREES_90\x10\x01\x12\x0f\n\x0b\x44\x45GREES_180\x10\x02\x12\x0f\n\x0b\x44\x45GREES_270\x10\x03\x12\x16\n\x12\x44\x45GREES_0_INVERTED\x10\x04\x12\x17\n\x13\x44\x45GREES_90_INVERTED\x10\x05\x12\x18\n\x14\x44\x45GREES_180_INVERTED\x10\x06\x12\x18\n\x14\x44\x45GREES_270_INVERTED\x10\x07\x1a\xdb\x06\n\nLoRaConfig\x12\x12\n\nuse_preset\x18\x01 \x01(\x08\x12H\n\x0cmodem_preset\x18\x02 \x01(\x0e\x32\x32.meshtastic.protobuf.Config.LoRaConfig.ModemPreset\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x15\n\rspread_factor\x18\x04 \x01(\r\x12\x13\n\x0b\x63oding_rate\x18\x05 \x01(\r\x12\x18\n\x10\x66requency_offset\x18\x06 \x01(\x02\x12\x41\n\x06region\x18\x07 \x01(\x0e\x32\x31.meshtastic.protobuf.Config.LoRaConfig.RegionCode\x12\x11\n\thop_limit\x18\x08 \x01(\r\x12\x12\n\ntx_enabled\x18\t \x01(\x08\x12\x10\n\x08tx_power\x18\n \x01(\x05\x12\x13\n\x0b\x63hannel_num\x18\x0b \x01(\r\x12\x1b\n\x13override_duty_cycle\x18\x0c \x01(\x08\x12\x1e\n\x16sx126x_rx_boosted_gain\x18\r \x01(\x08\x12\x1a\n\x12override_frequency\x18\x0e \x01(\x02\x12\x17\n\x0fpa_fan_disabled\x18\x0f \x01(\x08\x12\x17\n\x0fignore_incoming\x18g \x03(\r\x12\x13\n\x0bignore_mqtt\x18h \x01(\x08\"\xcd\x01\n\nRegionCode\x12\t\n\x05UNSET\x10\x00\x12\x06\n\x02US\x10\x01\x12\n\n\x06\x45U_433\x10\x02\x12\n\n\x06\x45U_868\x10\x03\x12\x06\n\x02\x43N\x10\x04\x12\x06\n\x02JP\x10\x05\x12\x07\n\x03\x41NZ\x10\x06\x12\x06\n\x02KR\x10\x07\x12\x06\n\x02TW\x10\x08\x12\x06\n\x02RU\x10\t\x12\x06\n\x02IN\x10\n\x12\n\n\x06NZ_865\x10\x0b\x12\x06\n\x02TH\x10\x0c\x12\x0b\n\x07LORA_24\x10\r\x12\n\n\x06UA_433\x10\x0e\x12\n\n\x06UA_868\x10\x0f\x12\n\n\x06MY_433\x10\x10\x12\n\n\x06MY_919\x10\x11\x12\n\n\x06SG_923\x10\x12\"\x94\x01\n\x0bModemPreset\x12\r\n\tLONG_FAST\x10\x00\x12\r\n\tLONG_SLOW\x10\x01\x12\x12\n\x0eVERY_LONG_SLOW\x10\x02\x12\x0f\n\x0bMEDIUM_SLOW\x10\x03\x12\x0f\n\x0bMEDIUM_FAST\x10\x04\x12\x0e\n\nSHORT_SLOW\x10\x05\x12\x0e\n\nSHORT_FAST\x10\x06\x12\x11\n\rLONG_MODERATE\x10\x07\x1a\xd6\x01\n\x0f\x42luetoothConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x45\n\x04mode\x18\x02 \x01(\x0e\x32\x37.meshtastic.protobuf.Config.BluetoothConfig.PairingMode\x12\x11\n\tfixed_pin\x18\x03 \x01(\r\x12\x1e\n\x16\x64\x65vice_logging_enabled\x18\x04 \x01(\x08\"8\n\x0bPairingMode\x12\x0e\n\nRANDOM_PIN\x10\x00\x12\r\n\tFIXED_PIN\x10\x01\x12\n\n\x06NO_PIN\x10\x02\x42\x11\n\x0fpayload_variantBa\n\x13\x63om.geeksville.meshB\x0c\x43onfigProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.protobuf.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\014ConfigProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _CONFIG_DEVICECONFIG_ROLE.values_by_name["ROUTER_CLIENT"]._options = None
  _CONFIG_DEVICECONFIG_ROLE.values_by_name["ROUTER_CLIENT"]._serialized_options = b'\010\001'
  _CONFIG_POSITIONCONFIG.fields_by_name['gps_enabled']._options = None
  _CONFIG_POSITIONCONFIG.fields_by_name['gps_enabled']._serialized_options = b'\030\001'
  _CONFIG_POSITIONCONFIG.fields_by_name['gps_attempt_time']._options = None
  _CONFIG_POSITIONCONFIG.fields_by_name['gps_attempt_time']._serialized_options = b'\030\001'
  _globals['_CONFIG']._serialized_start=58
  _globals['_CONFIG']._serialized_end=4630
  _globals['_CONFIG_DEVICECONFIG']._serialized_start=497
  _globals['_CONFIG_DEVICECONFIG']._serialized_end=1176
  _globals['_CONFIG_DEVICECONFIG_ROLE']._serialized_start=919
  _globals['_CONFIG_DEVICECONFIG_ROLE']._serialized_end=1093
  _globals['_CONFIG_DEVICECONFIG_REBROADCASTMODE']._serialized_start=1095
  _globals['_CONFIG_DEVICECONFIG_REBROADCASTMODE']._serialized_end=1176
  _globals['_CONFIG_POSITIONCONFIG']._serialized_start=1179
  _globals['_CONFIG_POSITIONCONFIG']._serialized_end=1845
  _globals['_CONFIG_POSITIONCONFIG_POSITIONFLAGS']._serialized_start=1619
  _globals['_CONFIG_POSITIONCONFIG_POSITIONFLAGS']._serialized_end=1790
  _globals['_CONFIG_POSITIONCONFIG_GPSMODE']._serialized_start=1792
  _globals['_CONFIG_POSITIONCONFIG_GPSMODE']._serialized_end=1845
  _globals['_CONFIG_POWERCONFIG']._serialized_start=1848
  _globals['_CONFIG_POWERCONFIG']._serialized_end=2108
  _globals['_CONFIG_NETWORKCONFIG']._serialized_start=2111
  _globals['_CONFIG_NETWORKCONFIG']._serialized_end=2511
  _globals['_CONFIG_NETWORKCONFIG_IPV4CONFIG']._serialized_start=2404
  _globals['_CONFIG_NETWORKCONFIG_IPV4CONFIG']._serialized_end=2474
  _globals['_CONFIG_NETWORKCONFIG_ADDRESSMODE']._serialized_start=2476
  _globals['_CONFIG_NETWORKCONFIG_ADDRESSMODE']._serialized_end=2511
  _globals['_CONFIG_DISPLAYCONFIG']._serialized_start=2514
  _globals['_CONFIG_DISPLAYCONFIG']._serialized_end=3532
  _globals['_CONFIG_DISPLAYCONFIG_GPSCOORDINATEFORMAT']._serialized_start=3078
  _globals['_CONFIG_DISPLAYCONFIG_GPSCOORDINATEFORMAT']._serialized_end=3155
  _globals['_CONFIG_DISPLAYCONFIG_DISPLAYUNITS']._serialized_start=3157
  _globals['_CONFIG_DISPLAYCONFIG_DISPLAYUNITS']._serialized_end=3197
  _globals['_CONFIG_DISPLAYCONFIG_OLEDTYPE']._serialized_start=3199
  _globals['_CONFIG_DISPLAYCONFIG_OLEDTYPE']._serialized_end=3276
  _globals['_CONFIG_DISPLAYCONFIG_DISPLAYMODE']._serialized_start=3278
  _globals['_CONFIG_DISPLAYCONFIG_DISPLAYMODE']._serialized_end=3343
  _globals['_CONFIG_DISPLAYCONFIG_COMPASSORIENTATION']._serialized_start=3346
  _globals['_CONFIG_DISPLAYCONFIG_COMPASSORIENTATION']._serialized_end=3532
  _globals['_CONFIG_LORACONFIG']._serialized_start=3535
  _globals['_CONFIG_LORACONFIG']._serialized_end=4394
  _globals['_CONFIG_LORACONFIG_REGIONCODE']._serialized_start=4038
  _globals['_CONFIG_LORACONFIG_REGIONCODE']._serialized_end=4243
  _globals['_CONFIG_LORACONFIG_MODEMPRESET']._serialized_start=4246
  _globals['_CONFIG_LORACONFIG_MODEMPRESET']._serialized_end=4394
  _globals['_CONFIG_BLUETOOTHCONFIG']._serialized_start=4397
  _globals['_CONFIG_BLUETOOTHCONFIG']._serialized_end=4611
  _globals['_CONFIG_BLUETOOTHCONFIG_PAIRINGMODE']._serialized_start=4555
  _globals['_CONFIG_BLUETOOTHCONFIG_PAIRINGMODE']._serialized_end=4611
# @@protoc_insertion_point(module_scope)
