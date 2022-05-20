import datetime
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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



# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context=context)

def genReport(request):
    context = {}
    return render(request, "genReport.html", context=context)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'id']
    filterset_fields = ['name', 'id']
    order_fields = ['id']

class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alerts.objects.all().order_by('name')
    serializer_class = AlertsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'id']
    filterset_fields = ['name', 'id']
    order_fields = ['id']

class InsurgentViewSet(viewsets.ModelViewSet):
    queryset = Insurgent.objects.all().order_by('id')
    serializer_class = InsurgentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class BritishViewSet(viewsets.ModelViewSet):
    queryset = British.objects.all().order_by('id')
    serializer_class = BritishSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class AustralianArmyViewSet(viewsets.ModelViewSet):
    queryset = AustralianArmy.objects.all().order_by('id')
    serializer_class = AustralianArmySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class CanadianArmyViewSet(viewsets.ModelViewSet):
    queryset = CanadianArmy.objects.all().order_by('id')
    serializer_class = CanadianArmySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class IrregularMilitiaViewSet(viewsets.ModelViewSet):
    queryset = IrregularMilitia.objects.all().order_by('id')
    serializer_class = IrregularMilitiaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class MiddleEasternAllianceViewSet(viewsets.ModelViewSet):
    queryset = MiddleEasternAlliance.objects.all().order_by('id')
    serializer_class = MiddleEasterAllianceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class PanAsiaViewSet(viewsets.ModelViewSet):
    queryset = PanAsia.objects.all().order_by('id')
    serializer_class = PanAsiaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class RussianGroundForcesViewSet(viewsets.ModelViewSet):
    queryset = RussianGroundForces.objects.all().order_by('id')
    serializer_class = RussianGroundForcesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class UnitedStatesArmyViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesArmy.objects.all().order_by('id')
    serializer_class = UnitedStatesArmySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

class UnitedStatesMarineCoreViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesMarineCore.objects.all().order_by('id')
    serializer_class = UnitedStatesMarineCoreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'isSquadRole']
    order_fields = ['id']

# Generate PDF
# def british_pdf(request):
#     # Create bytestream buffer
#     buf = io.BytesIO()
#     # Create Canvas
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     # Create Text Object
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 14)
#     britishs = British.objects.all()
#     # Create blank list
#     lines = [
#         "SquadKitResearch Team Development Role PDF's \n"
#         " PRIVATE USE "
#     ]

#     for british in britishs:
#         lines.append(" ")
#         lines.append("---------------------------------------------------------------------------------------- ")
#         lines.append(" ")
#         lines.append("/n")
#         lines.append("ROLE NAME: " + british.RoleName),
#         lines.append(" "),
#         lines.append("FACTION: " +british.faction),
#         lines.append(" "),
#         lines.append(british.PrimaryWeapon),
#         lines.append(" "),
#         lines.append(british.PrimaryWeaponSights),
#         lines.append(" "),
#         lines.append(british.PrimaryFiringModes),
#         lines.append(" "),
#         lines.append(str(british.PrimaryMagazineAmount)),
#         lines.append(" "),
#         lines.append(str(british.PrimaryMagazineRoundAmount)),
#         lines.append(" "),
#         lines.append(british.SecondaryWeapon),
#         lines.append(" "),
#         lines.append(british.c),
#         lines.append(" "),
#         lines.append(british.SecondaryWeaponFiringModes),
#         lines.append(" "),
#         lines.append(str(british.SecondaryWeaponMagAmount)),
#         lines.append(" "),
#         lines.append(str(british.SecondaryWeaponMagRoundAmount)),
#         lines.append(" "),
#         lines.append(british.Knife),
#         lines.append(" "),
#         lines.append(" "),

#     # Loop
#     for line in lines:
#         textob.textLine(line)
        
#     # Finish
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)

#     # Return
#     return FileResponse(buf, as_attachment=True, filename="Report.pdf")

def allReport(request):
    

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.image("https://storage.googleapis.com/skr-api/SKR.png", 180, 0, 25)
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_margin(1)
    pdf.set_author="SquadKitResearch"
    pdf.set_lang="en-US"
    pdf.set_auto_page_break=True
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Reports',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, 'All Faction Roles',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.ln(20)
    pdf.set_font('helvetica', '', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(210, 10, f"{'Role Information'.ljust(30)} {'ALL FACTIONS'.rjust(40)}", 0, 1, fill=True, align='L')
    britishs = British.objects.all()
    insurgents = Insurgent.objects.all()
    australians = AustralianArmy.objects.all()
    canadians = CanadianArmy.objects.all()
    irregularMilitia = IrregularMilitia.objects.all()
    middleEasternAlliance = MiddleEasternAlliance.objects.all()
    panAsia = PanAsia.objects.all()
    russianGroundForces = RussianGroundForces.objects.all()
    unitedStatesArmy = UnitedStatesArmy.objects.all()
    unitedStatesMarineCore = UnitedStatesMarineCore.objects.all()
    line = []
    for australian in australians:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {australian.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {australian.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {australian.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {australian.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {australian.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(australian.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(australian.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {australian.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {australian.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {australian.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(australian.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(australian.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {australian.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1325", x=140, y=280, w=4, h=10)
    for canadian in canadians:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {canadian.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {canadian.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {canadian.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {canadian.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {canadian.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(canadian.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(canadian.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {canadian.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {canadian.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {canadian.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(canadian.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(canadian.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {canadian.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1326", x=140, y=280, w=4, h=10)
    for canadian in canadians:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {canadian.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {canadian.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {canadian.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {canadian.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {canadian.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(canadian.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(canadian.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {canadian.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {canadian.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {canadian.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(canadian.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(canadian.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {canadian.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1327", x=140, y=280, w=4, h=10)
    for irregularMilitia in irregularMilitia:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {irregularMilitia.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {irregularMilitia.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {irregularMilitia.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {irregularMilitia.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {irregularMilitia.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(irregularMilitia.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(irregularMilitia.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {irregularMilitia.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {irregularMilitia.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {irregularMilitia.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(irregularMilitia.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(irregularMilitia.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {irregularMilitia.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1328", x=140, y=280, w=4, h=10)
    for middleEasternAlliance in middleEasternAlliance:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {middleEasternAlliance.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {middleEasternAlliance.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {middleEasternAlliance.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {middleEasternAlliance.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {middleEasternAlliance.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(middleEasternAlliance.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(middleEasternAlliance.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {middleEasternAlliance.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {middleEasternAlliance.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {middleEasternAlliance.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(middleEasternAlliance.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(middleEasternAlliance.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {middleEasternAlliance.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1329", x=140, y=280, w=4, h=10)
    for panAsia in panAsia:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {panAsia.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {panAsia.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {panAsia.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {panAsia.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {panAsia.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(panAsia.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(panAsia.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {panAsia.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {panAsia.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {panAsia.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(panAsia.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(panAsia.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {panAsia.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1330", x=140, y=280, w=4, h=10)
    for russianGroundForces in russianGroundForces:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {russianGroundForces.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {russianGroundForces.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {russianGroundForces.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {russianGroundForces.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {russianGroundForces.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(russianGroundForces.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(russianGroundForces.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {russianGroundForces.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {russianGroundForces.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {russianGroundForces.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(russianGroundForces.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(russianGroundForces.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {panAsia.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1331", x=140, y=280, w=4, h=10)
    for unitedStatesArmy in unitedStatesArmy:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {unitedStatesArmy.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {unitedStatesArmy.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {unitedStatesArmy.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {unitedStatesArmy.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {unitedStatesArmy.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(unitedStatesArmy.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(unitedStatesArmy.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {unitedStatesArmy.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {unitedStatesArmy.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {unitedStatesArmy.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(unitedStatesArmy.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(unitedStatesArmy.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {unitedStatesArmy.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1331", x=140, y=280, w=4, h=10)
    for unitedStatesArmy in unitedStatesArmy:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {unitedStatesArmy.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {unitedStatesArmy.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {unitedStatesArmy.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {unitedStatesArmy.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {unitedStatesArmy.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(unitedStatesArmy.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(unitedStatesArmy.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {unitedStatesArmy.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {unitedStatesArmy.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {unitedStatesArmy.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(unitedStatesArmy.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(unitedStatesArmy.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {unitedStatesArmy.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1332", x=140, y=280, w=4, h=10)
    for unitedStatesMarineCore in unitedStatesMarineCore:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {unitedStatesArmy.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {unitedStatesArmy.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {unitedStatesArmy.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {unitedStatesArmy.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {unitedStatesArmy.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(unitedStatesArmy.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(unitedStatesArmy.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {unitedStatesArmy.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {unitedStatesArmy.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {unitedStatesArmy.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(unitedStatesArmy.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(unitedStatesArmy.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {unitedStatesArmy.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1333", x=140, y=280, w=4, h=10)
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
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1334", x=140, y=280, w=4, h=10)
    for insurgent in insurgents:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {insurgent.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {insurgent.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {insurgent.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {insurgent.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {insurgent.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(insurgent.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(insurgent.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {insurgent.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {insurgent.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {insurgent.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(insurgent.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(insurgent.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {insurgent.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        pdf.set_fill_color(0, 0, 0)
        pdf.interleaved2of5("1335", x=140, y=280, w=4, h=10)

    pdf.output('All-Factions-Report.pdf', 'F')
    return FileResponse(open('All-Factions-Report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

def britishReport(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.image("https://storage.googleapis.com/skr-api/SKR.png", 180, 0, 25)
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_margin(1)
    pdf.set_author="SquadKitResearch"
    pdf.set_lang="en-US"
    pdf.set_auto_page_break=True
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Reports',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, 'All British Roles',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(210, 10, f"{'Role Information'.ljust(30)} {'British FACTION'.rjust(40)}", 0, 1, fill=True, align='L')
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
    pdf.set_fill_color(0, 0, 0)
    pdf.interleaved2of5("1336", x=140, y=280, w=4, h=10)
   
    pdf.output('British-Report.pdf', 'F')
    return FileResponse(open('British-Report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

def insurgentReport(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.image("https://storage.googleapis.com/skr-api/SKR.png", 180, 0, 25)
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_margin(1)
    pdf.set_author="SquadKitResearch"
    pdf.set_lang="en-US"
    pdf.set_auto_page_break=True
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Reports',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, 'All Insurgent Roles',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(210, 10, f"{'Role Information'.ljust(30)} {'Insurgent FACTION'.rjust(40)}", 0, 1, fill=True, align='L')
    
    # pdf.line(0, 61, 210, 61)
    # pdf.line(0, 71, 210, 71)
    insurgents = Insurgent.objects.all()
    line = []
    for insurgent in insurgents:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {insurgent.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {insurgent.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {insurgent.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON 2: {insurgent.PrimaryWeapon_2.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {insurgent.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {insurgent.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(insurgent.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY 2 MAG AMOUNT: {str(insurgent.Primary_2_MagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(insurgent.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY 2 ROUNDS PER MAG AMOUNT: {str(insurgent.Primary_2_MagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {insurgent.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {insurgent.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {insurgent.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(insurgent.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(insurgent.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {insurgent.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
    pdf.set_fill_color(0, 0, 0)
    pdf.interleaved2of5("1337", x=140, y=280, w=4, h=10)
    pdf.output('Insurgent-Report.pdf', 'F')
    return FileResponse(open('Insurgent-Report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

def australianReport(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.image("https://storage.googleapis.com/skr-api/SKR.png", 180, 0, 25)
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_margin(1)
    pdf.set_author="SquadKitResearch"
    pdf.set_lang="en-US"
    pdf.set_auto_page_break=True
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Reports',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, 'All Australian Roles',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(210, 10, f"{'Role Information'.ljust(30)} {'Australian FACTION'.rjust(40)}", 0, 1, fill=True, align='L')
    australians = AustralianArmy.objects.all()
    line = []
    for australian in australians:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {australian.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {australian.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {australian.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {australian.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {australian.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(australian.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(australian.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {australian.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {australian.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {australian.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(australian.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(australian.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {australian.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
    pdf.set_fill_color(0, 0, 0)
    pdf.interleaved2of5("1338", x=120, y=130, w=4, h=10)
   
    pdf.output('Australian-Report.pdf', 'F')
    return FileResponse(open('Australian-Report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

def canadianReport(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.image("https://storage.googleapis.com/skr-api/SKR.png", 180, 0, 25)
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_margin(1)
    pdf.set_author="SquadKitResearch"
    pdf.set_lang="en-US"
    pdf.set_auto_page_break=True
    pdf.cell(40, 10, 'SquadKitResearch Automatically Generated PDF Reports',0,1)
    pdf.cell(40, 10, 'INSIDE USE ONLY',0,1)
    pdf.cell(40, 10, 'All Canadian Roles',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('helvetica', '', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(210, 10, f"{'Role Information'.ljust(30)} {'Canadian FACTION'.rjust(40)}", 0, 1, fill=True, align='L')
    canadians = CanadianArmy.objects.all()
    line = []
    for canadian in canadians:
        line.append(pdf.cell(200, 8, f" ", 0, 1))
        line.append(pdf.cell(200, 8, f"ROLE NAME: {canadian.RoleName.ljust(50)}", 2, 2))
        line.append(pdf.cell(200, 8, f"FACTION: {canadian.faction.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON: {canadian.PrimaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON SIGHTS: {canadian.PrimaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY WEAPON FIRING MODES: {canadian.PrimaryFiringModes.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PRIMARY MAG AMOUNT: {str(canadian.PrimaryMagazineAmount).rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"PIMARY ROUNDS PER MAG AMOUNT: {str(canadian.PrimaryMagazineRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON: {canadian.SecondaryWeapon.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON SIGHTS: {canadian.SecondaryWeaponSights.rjust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON FIRING MODES: {canadian.SecondaryWeaponFiringModes.ljust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY WEAPON MAG AMOUNT: {str(canadian.SecondaryWeaponMagAmount).rjust(1)} ", 0, 1))
        line.append(pdf.cell(200, 8, f"SECONDARY ROUNDS PER MAG AMOUNT: {str(canadian.SecondaryWeaponMagRoundAmount).ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f"KNIFE: {canadian.Knife.ljust(1)}", 0, 1))
        line.append(pdf.cell(200, 8, f" ", 0, 1))
    pdf.set_fill_color(0, 0, 0)
    pdf.interleaved2of5("1339", x=120, y=130, w=4, h=10)
   
    pdf.output('Canadian-Report.pdf', 'F')
    return FileResponse(open('Canadian-Report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')