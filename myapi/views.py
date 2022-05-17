from encodings import search_function
from http.client import HTTPResponse
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import AlertsSerializer, AustralianArmySerializer, BritishSerializer, CanadianArmySerializer, InsurgentSerializer, IrregularMilitiaSerializer, MiddleEasterAllianceSerializer, PanAsiaSerializer, PostSerializer, RussianGroundForcesSerializer, UnitedStatesArmySerializer, UnitedStatesMarineCoreSerializer
from .models import Alerts, AustralianArmy, British, CanadianArmy, IrregularMilitia, Post, Insurgent, MiddleEasternAlliance, PanAsia, RussianGroundForces, UnitedStatesArmy, UnitedStatesMarineCore


# Genereating PDF's
from fpdf import FPDF
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from textwrap import wrap

styles = getSampleStyleSheet()



# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context=context)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'id']
    filterset_fields = ['name', 'id']

class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alerts.objects.all().order_by('name')
    serializer_class = AlertsSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'id']
    filterset_fields = ['name', 'id']

class InsurgentViewSet(viewsets.ModelViewSet):
    queryset = Insurgent.objects.all().order_by('id')
    serializer_class = InsurgentSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class BritishViewSet(viewsets.ModelViewSet):
    queryset = British.objects.all().order_by('id')
    serializer_class = BritishSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class AustralianArmyViewSet(viewsets.ModelViewSet):
    queryset = AustralianArmy.objects.all().order_by('id')
    serializer_class = AustralianArmySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class CanadianArmyViewSet(viewsets.ModelViewSet):
    queryset = CanadianArmy.objects.all().order_by('id')
    serializer_class = CanadianArmySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class IrregularMilitiaViewSet(viewsets.ModelViewSet):
    queryset = IrregularMilitia.objects.all().order_by('id')
    serializer_class = IrregularMilitiaSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class MiddleEasternAllianceViewSet(viewsets.ModelViewSet):
    queryset = MiddleEasternAlliance.objects.all().order_by('id')
    serializer_class = MiddleEasterAllianceSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class PanAsiaViewSet(viewsets.ModelViewSet):
    queryset = PanAsia.objects.all().order_by('id')
    serializer_class = PanAsiaSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class RussianGroundForcesViewSet(viewsets.ModelViewSet):
    queryset = RussianGroundForces.objects.all().order_by('id')
    serializer_class = RussianGroundForcesSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class UnitedStatesArmyViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesArmy.objects.all().order_by('id')
    serializer_class = UnitedStatesArmySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class UnitedStatesMarineCoreViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesMarineCore.objects.all().order_by('id')
    serializer_class = UnitedStatesMarineCoreSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

# Generate PDF
def british_pdf(request):
    # Create bytestream buffer
    buf = io.BytesIO()
    # Create Canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create Text Object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    style = styles["Normal"]


    # Add lines of text
    # lines = [
    #     'Line 1',
    #     'Line 2',
    #     'Line 3',
    #     'Line 4',
    # ]

    britishs = British.objects.all()
    # Create blank list
    lines = [
        "SquadKitResearch Team Development Role PDF's \n"
        " PRIVATE USE "
    ]

    for british in britishs:
        lines.append(" ")
        lines.append("---------------------------------------------------------------------------------------- ")
        lines.append(" ")
        lines.append("/n")
        lines.append("ROLE NAME: " + british.RoleName),
        lines.append(" "),
        lines.append("FACTION: " +british.faction),
        lines.append(" "),
        lines.append(british.PrimaryWeapon),
        lines.append(" "),
        lines.append(british.PrimaryWeaponSights),
        lines.append(" "),
        lines.append(british.PrimaryFiringModes),
        lines.append(" "),
        lines.append(str(british.PrimaryMagazineAmount)),
        lines.append(" "),
        lines.append(str(british.PrimaryMagazineRoundAmount)),
        lines.append(" "),
        lines.append(british.SecondaryWeapon),
        lines.append(" "),
        lines.append(british.c),
        lines.append(" "),
        lines.append(british.SecondaryWeaponFiringModes),
        lines.append(" "),
        lines.append(str(british.SecondaryWeaponMagAmount)),
        lines.append(" "),
        lines.append(str(british.SecondaryWeaponMagRoundAmount)),
        lines.append(" "),
        lines.append(british.Knife),
        lines.append(" "),
        lines.append(" "),

    # Loop
    for line in lines:
        textob.textLine(line)
        
    # Finish
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return
    return FileResponse(buf, as_attachment=True, filename="Report.pdf")

def report(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Files',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(200, 8, f"{'Role Name'.ljust(30)} {'Faction'.rjust(40)}", 0, 1)
    pdf.line(10, 40, 190, 40)
    pdf.line(10, 48, 190, 48)
    britishs = British.objects.all()
    line = []
    for british in britishs:
        line.append(pdf.cell(200, 8, f"{british.RoleName.ljust(30)} {british.faction.rjust(20)}", 0, 1))
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(200, 8, f"{'Role Weapons'.ljust(30)} {'Weapon Magazine'.rjust(40)} {'Round per mag'.rjust(40)} ", 0, 1)
    pdf.line(10, 73, 190, 73)
    pdf.line(10, 81, 190, 81)
    for british in britishs:
        line.append(pdf.cell(200, 8, f"{british.PrimaryWeapon.ljust(30)} {str(british.PrimaryMagazineAmount).rjust(20)} {str(british.PrimaryMagazineRoundAmount).rjust(60)}", 0, 1)),
        line.append(pdf.cell(200, 8, f"{british.SecondaryWeapon.ljust(30)} {str(british.SecondaryWeaponMagAmount).rjust(29)} {str(british.SecondaryWeaponMagRoundAmount).rjust(61)}", 0, 1)),

    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(200, 8, f"{'Primary Weapon Sights'.ljust(30)} {'Secondary Weapon Sights'.rjust(45)}", 0, 1)
    pdf.line(10, 123, 190, 123)
    pdf.line(10, 131, 190, 131)
    for british in britishs:
        line.append(pdf.cell(200, 8, f"{british.PrimaryWeaponSights.ljust(30)} {str(british.SecondaryWeaponSights).rjust(50)}", 0, 1)),

    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(200, 8, f"{'Primary Weapon Firing Mode'.ljust(30)} {'Secondary Weapon Firing Mode'.rjust(45)}", 0, 1)
    pdf.line(10, 157, 190, 157)
    pdf.line(10, 165, 190, 165)
    for british in britishs:
        line.append(pdf.cell(200, 8, f"{british.PrimaryFiringModes.ljust(30)} {str(british.SecondaryWeaponFiringModes).rjust(40)}", 0, 1)),
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


def britishReport(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Files',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(210, 10, f"{'Role Information'.ljust(30)} {'Faction'.rjust(40)}", 0, 1)
    pdf.line(10, 40, 190, 40)
    pdf.line(10, 48, 190, 48)
    britishs = British.objects.all()
    line = []
    for british in britishs:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {british.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {british.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {british.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {british.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {british.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(british.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(british.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {british.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {british.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {british.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(british.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(british.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {british.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
   
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


# pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
#     pdf.cell(40, 10, '',0,1)
#     pdf.set_font('courier', '', 12)
#     pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
#     pdf.line(10, 30, 150, 30)
#     pdf.line(10, 38, 150, 38)