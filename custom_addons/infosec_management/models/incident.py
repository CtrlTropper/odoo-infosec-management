# -*- coding: utf-8 -*-
from odoo import models, fields


class InfosecIncident(models.Model):
    _name = "infosec.incident"
    _description = "Ghi nhận Sự cố Bảo mật"

    name = fields.Char(
        string="Mã Sự Cố", required=True, copy=False, readonly=True, default="New"
    )
    title = fields.Char(string="Tiêu đề", required=True)

    # Quan hệ Many2one: Một sự cố thuộc về một thiết bị
    asset_id = fields.Many2one(
        "infosec.asset", string="Thiết bị liên quan", ondelete="restrict"
    )

    severity = fields.Selection(
        [
            ("low", "Thấp"),
            ("medium", "Trung bình"),
            ("high", "Cao"),
            ("critical", "Nghiêm trọng (Critical)"),
        ],
        string="Mức độ",
        required=True,
    )

    description = fields.Text(string="Mô tả chi tiết")

    # Trường dữ liệu đặc biệt này rất quan trọng để lưu log thô (Raw Log).
    # Sau này ở Phase 5, API sẽ kéo dữ liệu ở đây ném vào Vinallama 2.7B để phân tích.
    raw_log_data = fields.Text(
        string="Raw Security Log",
        help="Lưu log thô từ thiết bị (Syslog/SNMP) để AI đánh giá",
    )
