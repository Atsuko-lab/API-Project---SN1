from rest_framework.response import Response
from rest_framework.decorators import api_view
from .open_ai_service import open_ia_response
import json

@api_view(['GET'])
def accueil_eleve(request):
    return Response("Bienvenue dans le service d'aide à l'élève! Tu peux avoir accès aux routes /resume, /explique, /entrainement et /question. Bon courage !")

@api_view(['POST'])
def resume(request):
    cours = request.data.get('cours')
    
    prompt = f"Fais un résumé court de ce texte : {cours}"
    resume = open_ia_response(prompt)
    
    return Response({"Resumé": resume})

@api_view(['POST'])
def explication(request):
    idée = request.data.get('idée')
    niveau = request.data.get('level')

    prompt = f"Explique le concept '{idée}' à un niveau {niveau}."
    explanation = open_ia_response(prompt)
    
    return Response({"Explication": explanation})

@api_view(['POST'])
def quiz(request):
    sujet = request.data.get('sujet')
    level = request.data.get('level')

    prompt = f"Génère 5 questions à choix multiples sur {sujet} pour un niveau {level}. Réponds sous ce format JSON : " \
             "[{\"question\": \"...\", \"options\": [\"...\", \"...\", \"...\"], \"answer\": \"...\"}]"

    quiz_response = open_ia_response(prompt)
    quiz = json.loads(quiz_response)

    return Response({"Quiz": quiz})


@api_view(['POST'])
def chat_with_gpt(request):
    question = request.data.get('question')

    response = open_ia_response(question)
    
    return Response({"Réponse": response})


