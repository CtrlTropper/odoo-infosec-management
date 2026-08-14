# -*- coding: utf-8 -*-
from odoo import models, fields

class InfosecAsset(models.Model):
    _name = 'infosec.asset'
    _description = 'Thông tin Thiết bị Mạng & Bảo mật'

    name = fields.Char(string='Tên thiết bị', required=True, help="Ví dụ: FW-DC-PaloAlto-01")
    ip_address = fields.Char(string='Địa chỉ IP')
    
    # Chuẩn hóa các thiết bị em thường xuyên làm việc trong lab và thực tế
    device_type = fields.Selection([
        ('cisco_ios', 'Cisco IOS'),
        ('pan_os', 'Palo Alto PAN-OS'),
        ('stormshield', 'Stormshield Network Security'),
        ('eve_ng', 'EVE-NG / GNS3 Node')
    ], string='Hệ điều hành / Loại', required=True)
    
    status = fields.Selection([
        ('active', 'Đang hoạt động'),
        ('maintenance', 'Đang bảo trì'),
        ('compromised', 'Nghi ngờ xâm nhập (Compromised)')
    ], string='Trạng thái', default='active')