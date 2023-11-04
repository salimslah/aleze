from odoo import api,fields,models

class Doctor(models.Model):
    _name = "hospital.doctor"
    _description = "hosptial doctors record"
    _inherit="mail.thread" #inherit from othor module for traking
    _rec_name ="ref"   # if you want to display ref field insted of name 



    name = fields.Char(string="Name" ,required=True ,tracking=True)
    ref= fields.Char(string="Refrence" ,required=True ,tracking=True)
    gender = fields.Selection([("male","Male"),("fmale","Fmale"),("othor","Othor")],string="Gender" ,tracking=True)
    active =fields.Boolean(default=True)




    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res


