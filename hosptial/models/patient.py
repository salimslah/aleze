from odoo import api,fields,models ,_
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = "hospital.patient"
    _description="hosptial patient record"
    _inherit="mail.thread" #inherit from othor module for traking
    
    name = fields.Char(string ="Name",required = "True", tracking=True)
    age = fields.Integer(string ="Age", tracking = True)
    is_child = fields.Boolean(string ="Is Child ?", tracking =True)
    notes = fields.Text(string ="Notes", tracking = True)
    gender = fields.Selection([("male","Male"),("female","Female"),("others","Others")],string ="Gender" , tracking=True)
    captalized_name = fields.Char(string ="Captalized_name", compute ="_compute_captalized_name" ,store=True)
    ref = fields.Char(string ="Refrence" , default=lambda self:_("New"))
    doctor_id =fields.Many2one('hospital.doctor' ,string="doctors")
    tags_ids = fields.Many2many('res.partner.category','hospital_patient_tag_record' ,'patient_name' , 'patient_id', string="tags")

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals["ref"] = self.env['ir.sequence'].next_by_code("hospital_pateint")
        return super(Patient,self).create(vals_list)


    @api.constrains("is_child","age")
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("age has to be recorded"))

    @api.depends("name")
    def _compute_captalized_name(self):
        for rec in self:
            if self.name:
                self.captalized_name =self.name.upper()
            else:
                self.captalized_name = ""


    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False













