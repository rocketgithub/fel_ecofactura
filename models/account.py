# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from datetime import datetime
from lxml import etree
import base64
import logging
import zeep

class AccountMove(models.Model):
    _inherit = "account.move"

    pdf_fel = fields.Binary('PDF FEL', copy=False)
    pdf_fel_name = fields.Char('Nombre PDF FEL', default='pdf_fel.pdf', size=32)

    def post(self):
        for factura in self:
            if factura.requiere_certificacion():

                if factura.error_pre_validacion():
                    return

                stdTWS = etree.Element("stdTWS", xmlns="FEL")

                TrnEstNum = etree.SubElement(stdTWS, "TrnEstNum")
                TrnEstNum.text = str(factura.journal_id.codigo_establecimiento)
                TipTrnCod = etree.SubElement(stdTWS, "TipTrnCod")
                TipTrnCod.text = factura.journal_id.tipo_documento_fel
                TrnNum = etree.SubElement(stdTWS, "TrnNum")
                TrnNum.text = str(factura.id)
                TrnFec = etree.SubElement(stdTWS, "TrnFec")
                TrnFec.text = factura.invoice_date.strftime('%Y-%m-%d')
                MonCod = etree.SubElement(stdTWS, "MonCod")
                MonCod.text = "GTQ"
                TrnBenConNIT = etree.SubElement(stdTWS, "TrnBenConNIT")
                TrnBenConNIT.text = factura.partner_id.vat.replace('-', '') or ''
                TrnFec = etree.SubElement(stdTWS, "TrnExp")
                TrnFec.text = "1" if factura.tipo_gasto == "importacion" else "0"
                TrnFec = etree.SubElement(stdTWS, "TrnExento")
                TrnFec.text = "0"
                TrnFec = etree.SubElement(stdTWS, "TrnFraseTipo")
                TrnFec.text = "0"
                TrnFec = etree.SubElement(stdTWS, "TrnEscCod")
                TrnFec.text = "1" if factura.tipo_gasto == "importacion" else "0"
                TrnEFACECliCod = etree.SubElement(stdTWS, "TrnEFACECliCod")
                TrnEFACECliNom = etree.SubElement(stdTWS, "TrnEFACECliNom")
                TrnEFACECliNom.text = factura.partner_id.name
                TrnEFACECliDir = etree.SubElement(stdTWS, "TrnEFACECliDir")
                TrnEFACECliDir.text = factura.partner_id.street or ""
                TrnObs = etree.SubElement(stdTWS, "TrnObs")
                TrnObs.text = factura.motivo_fel or ""
                TrnEMail = etree.SubElement(stdTWS, "TrnEmail")
                if factura.partner_id.email:
                    TrnEMail.text = factura.partner_id.email
                TrnCampAd01 = etree.SubElement(stdTWS, "TrnCampAd01")
                TrnCampAd01.text = eval(factura.company_id.trncampad01_fel) if factura.company_id.trncampad01_fel else ""
                TrnCampAd02 = etree.SubElement(stdTWS, "TrnCampAd02")
                TrnCampAd02.text = eval(factura.company_id.trncampad02_fel) if factura.company_id.trncampad02_fel else ""
                TrnCampAd03 = etree.SubElement(stdTWS, "TrnCampAd03")
                TrnCampAd03.text = eval(factura.company_id.trncampad03_fel) if factura.company_id.trncampad03_fel else ""
                TrnCampAd04 = etree.SubElement(stdTWS, "TrnCampAd04")
                TrnCampAd04.text = eval(factura.company_id.trncampad04_fel) if factura.company_id.trncampad04_fel else ""
                TrnCampAd05 = etree.SubElement(stdTWS, "TrnCampAd05")
                TrnCampAd05.text = eval(factura.company_id.trncampad05_fel) if factura.company_id.trncampad05_fel else ""
                TrnCampAd06 = etree.SubElement(stdTWS, "TrnCampAd06")
                TrnCampAd06.text = eval(factura.company_id.trncampad06_fel) if factura.company_id.trncampad06_fel else ""
                TrnCampAd07 = etree.SubElement(stdTWS, "TrnCampAd07")
                TrnCampAd08 = etree.SubElement(stdTWS, "TrnCampAd08")
                TrnCampAd09 = etree.SubElement(stdTWS, "TrnCampAd09")
                TrnCampAd10 = etree.SubElement(stdTWS, "TrnCampAd10")
                TrnCampAd11 = etree.SubElement(stdTWS, "TrnCampAd11")
                TrnCampAd12 = etree.SubElement(stdTWS, "TrnCampAd12")
                TrnCampAd13 = etree.SubElement(stdTWS, "TrnCampAd13")
                TrnCampAd14 = etree.SubElement(stdTWS, "TrnCampAd14")
                TrnCampAd15 = etree.SubElement(stdTWS, "TrnCampAd15")
                TrnCampAd16 = etree.SubElement(stdTWS, "TrnCampAd16")
                TrnCampAd17 = etree.SubElement(stdTWS, "TrnCampAd17")
                TrnCampAd18 = etree.SubElement(stdTWS, "TrnCampAd18")
                TrnCampAd19 = etree.SubElement(stdTWS, "TrnCampAd19")
                TrnCampAd20 = etree.SubElement(stdTWS, "TrnCampAd20")
                TrnCampAd21 = etree.SubElement(stdTWS, "TrnCampAd21")
                TrnCampAd22 = etree.SubElement(stdTWS, "TrnCampAd22")
                TrnCampAd23 = etree.SubElement(stdTWS, "TrnCampAd23")
                TrnCampAd24 = etree.SubElement(stdTWS, "TrnCampAd24")
                TrnCampAd25 = etree.SubElement(stdTWS, "TrnCampAd25")
                TrnCampAd26 = etree.SubElement(stdTWS, "TrnCampAd26")
                TrnCampAd27 = etree.SubElement(stdTWS, "TrnCampAd27")
                TrnCampAd28 = etree.SubElement(stdTWS, "TrnCampAd28")
                TrnCampAd29 = etree.SubElement(stdTWS, "TrnCampAd29")
                TrnCampAd30 = etree.SubElement(stdTWS, "TrnCampAd30")
                
                stdTWSD = etree.SubElement(stdTWS, "stdTWSD")

                num = 1
                for linea in factura.invoice_line_ids:
                    stdTWSDIt = etree.SubElement(stdTWSD, "stdTWS.stdTWSCIt.stdTWSDIt")

                    TrnLiNum = etree.SubElement(stdTWSDIt, "TrnLiNum")
                    TrnLiNum.text = str(num)
                    num += 1
                    TrnArtCod = etree.SubElement(stdTWSDIt, "TrnArtCod")
                    if linea.product_id.default_code:
                        TrnArtCod.text = linea.product_id.default_code
                    else:
                        TrnArtCod.text = str(linea.product_id.id)
                    TrnArtNom = etree.SubElement(stdTWSDIt, "TrnArtNom")
                    TrnArtNom.text = linea.name
                    TrnCan = etree.SubElement(stdTWSDIt, "TrnCan")
                    TrnCan.text = str(linea.quantity)
                    TrnVUn = etree.SubElement(stdTWSDIt, "TrnVUn")
                    TrnVUn.text = '{:.6f}'.format(linea.price_unit)
                    TrnUniMed = etree.SubElement(stdTWSDIt, "TrnUniMed")
                    TrnUniMed.text = "UNIDAD"
                    TrnVDes = etree.SubElement(stdTWSDIt, "TrnVDes")
                    TrnVDes.text = '{:.6f}'.format(( linea.price_unit * linea.quantity ) *  ( linea.discount / 100 ))
                    TrnArtBienSer = etree.SubElement(stdTWSDIt, "TrnArtBienSer")
                    if linea.product_id.type == 'product':
                        TrnArtBienSer.text = "B"
                    else:
                        TrnArtBienSer.text = "S"
                    TrnArtImpAdiCod = etree.SubElement(stdTWSDIt, "TrnArtImpAdiCod")
                    TrnArtImpAdiCod.text = "0"
                    TrnArtImpAdiUniGrav = etree.SubElement(stdTWSDIt, "TrnArtImpAdiUniGrav")
                    TrnArtImpAdiUniGrav.text = "0"
                    TrnDetCampAd01 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi01")
                    TrnDetCampAd02 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi02")
                    TrnDetCampAd03 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi03")
                    TrnDetCampAd04 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi04")
                    TrnDetCampAd05 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi05")

                if factura.journal_id.tipo_documento_fel == "FCAM":
                    stdTWSCam = etree.SubElement(stdTWS, "stdTWSCam")
                    stdTWSCamIt = etree.SubElement(stdTWSCam, "stdTWS.stdTWSCam.stdTWSCamIt")
                    TrnAbonoNum = etree.SubElement(stdTWSCamIt, "TrnAbonoNum")
                    TrnAbonoNum.text = "1"
                    TrnAbonoFecVen = etree.SubElement(stdTWSCamIt, "TrnAbonoFecVen")
                    TrnAbonoFecVen.text = str(factura.date_due)
                    TrnAbonoMonto = etree.SubElement(stdTWSCamIt, "TrnAbonoMonto")
                    TrnAbonoMonto.text = str(factura.amount_total)
                    
                if factura.journal_id.tipo_documento_fel in ["NCRE", "NDEB"]:
                    stdTWSCam = etree.SubElement(stdTWS, "stdTWSNota")
                    stdTWSCamIt = etree.SubElement(stdTWSCam, "stdTWS.stdTWSNota.stdTWSNotaIt")
                    TDFEPRegimenAntiguo = etree.SubElement(stdTWSCamIt, "TDFEPRegimenAntiguo")
                    TDFEPRegimenAntiguo.text = "0"
                    TDFEPAutorizacion = etree.SubElement(stdTWSCamIt, "TDFEPAutorizacion")
                    TDFEPAutorizacion.text = factura.factura_original_id.firma_fel if factura.factura_original_id else ""
                    TDFEPSerie = etree.SubElement(stdTWSCamIt, "TDFEPSerie")
                    TDFEPSerie.text = factura.factura_original_id.serie_fel if factura.factura_original_id else ""
                    TDFEPNumero = etree.SubElement(stdTWSCamIt, "TDFEPNumero")
                    TDFEPNumero.text = factura.factura_original_id.numero_fel if factura.factura_original_id else ""
                    TDFEPNumero = etree.SubElement(stdTWSCamIt, "TDFEPFecEmision")
                    TDFEPNumero.text = str(factura.factura_original_id.invoice_date.strftime('%Y-%m-%d')) if factura.factura_original_id else ""

                xmls = etree.tostring(stdTWS, xml_declaration=True, encoding="UTF-8")
                logging.warn(xmls.decode('utf8'))

                wsdl = "https://www.facturaenlineagt.com/adocumento?wsdl"
                if factura.company_id.pruebas_fel:
                    wsdl = "http://pruebas.ecofactura.com.gt:8080/fel/adocumento?wsdl"
                client = zeep.Client(wsdl=wsdl)

                resultado = client.service.Execute(factura.company_id.vat, factura.company_id.usuario_fel, factura.company_id.clave_fel, factura.company_id.vat, xmls)
                logging.warn(resultado)
                resultadoBytes = bytes(bytearray(resultado, encoding='utf-8'))
                resultadoXML = etree.XML(resultadoBytes)

                if resultadoXML.xpath("/DTE"):
                    dte = resultadoXML.xpath("/DTE")
                    factura.name = dte[0].get("Serie")+"-"+dte[0].get("Numero")
                    factura.firma_fel = dte[0].get("NumeroAutorizacion")
                    factura.serie_fel = dte[0].get("Serie")
                    factura.numero_fel = dte[0].get("Numero")
                    factura.pdf_fel = resultadoXML.xpath("/DTE/Pdf")[0].text
                    factura.documento_xml_fel = base64.b64encode(b" "+xmls)
                    factura.resultado_xml_fel = resultadoXML.xpath("/DTE/Xml")[0].text
                    factura.certificador_fel = "ecofactura"
                else:
                    factura.error_certificador(resultado)
                    return

                return super(AccountMove,self).post()

            else:
                return super(AccountMove,self).post()
        
    def button_cancel(self):
        result = super(AccountMove, self).button_cancel()
        for factura in self:
            if factura.requiere_certificacion() and factura.firma_fel:
                
                wsdl = "https://www.facturaenlineagt.com/aanulacion?wsdl"
                if factura.company_id.pruebas_fel:
                    wsdl = "http://pruebas.ecofactura.com.gt:8080/fel/aanulacion?wsdl"
                client = zeep.Client(wsdl=wsdl)
                
                resultado = client.service.Execute(factura.company_id.vat, factura.company_id.usuario_fel, factura.company_id.clave_fel, factura.company_id.vat, factura.firma_fel, factura.motivo_fel)
                logging.warn(resultado)
                resultadoBytes = bytes(bytearray(resultado, encoding='utf-8'))
                resultadoXML = etree.XML(resultadoBytes)
                factura.pdf_fel = resultadoXML.xpath("/DTE/Pdf")[0].text
                logging.warn(resultado)
                
                if not resultadoXML.xpath("/DTE"):
                    raise ValidationError(resultado)
                                                
class AccountJournal(models.Model):
    _inherit = "account.journal"

class ResCompany(models.Model):
    _inherit = "res.company"

    usuario_fel = fields.Char('Usuario FEL')
    clave_fel = fields.Char('Clave FEL')
    pruebas_fel = fields.Boolean('Pruebas FEL')
    trncampad01_fel = fields.Char(string="TrnCampAd01 FEL")
    trncampad02_fel = fields.Char(string="TrnCampAd02 FEL")
    trncampad03_fel = fields.Char(string="TrnCampAd03 FEL")
    trncampad04_fel = fields.Char(string="TrnCampAd04 FEL")
    trncampad05_fel = fields.Char(string="TrnCampAd05 FEL")
    trncampad06_fel = fields.Char(string="TrnCampAd06 FEL")
