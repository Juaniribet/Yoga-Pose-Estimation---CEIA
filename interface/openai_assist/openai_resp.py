import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('MODEL')

def yoga_assistant_response(system_prompt, user_prompt):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1
    )
    
    return response

def yoga_assistant(report):
    replace_dict = {11 : "hombro derecho",
                    12 : "hombro izquierdo",
                    13 : "codo derecho",
                    14 : "codo izquierdo",
                    23 : "cadera derecha",
                    24 : "cadera izquierda",
                    25 : "rodilla derecha",
                    26 : "rodilla izquierda"}

    report['punto'] = report['punto'].replace(replace_dict)

    text_dic = {}
    for p in report['pose'].unique():
        text_dic1 = {}
        for i in range(report[report['pose'] == p].shape[0]-1):
            text_dic2 = {}
            for c in list(report.columns)[2:]:
                text_dic2[c] = list(report[report['pose'] == p][c])[i]
            text_dic1[list(report[report['pose'] == p]['punto'])[i]] = text_dic2
        text_dic[p] = text_dic1

    sist_prompt_yoga = """Eres un experto en la practica de yoga y en corregir posturas de Yoga de aprendices. 
    De un video de un usuario haciendo yoga se extrajo los angulos que forman las partes del cuerpo para poder entender si la postura se esta realizando en forma correcta
    Los datos estan en formato de json en donde primero se indica la parte del cuento y luego se indica el angulo optimo que se deberia obtener en esa parte del cuerpo, en angulo medio medido que es el valor medio que se obtuvo durante todo el tiempo que el usuario hizo la psotura
    y el mejor angulo alcanzado con la siguiente estructura:
    "{postura:{'ang optimo' : 'valor de angulo optimo', 'ang medido medio' : 'valor angulo medio medido', 'ang optimo' : 'valor de mejor angulo alcanzado'}}"
    Puedes verificar la diferencia: diferencia = abs('valor de angulo optimo' - 'valor angulo medio medido')
    Cuanta mayor diferencia haya entre el valor medio medido y el valor optimo peor posicionada esa parte del cuerpo y va a necesitar mayor correccion.
    Si la diferencia es mayor a 15 se vera en rojo y algo hay que decir.
    Analizar los siguientes valore e indicar si la postura se realizo en forma correcta y sugerencias para mejorar.
    Se amable en la respuesta siempre buscando la mejora fisica y mental de usuario.
    La respuesta no debe ser mayor a 200 palabras"""

    dic_poses_resp = {}

    for i in range(len(list(text_dic.keys()))):
        posture_data = f'De la postura de yoga {list(text_dic.keys())[i]} de obtuvieron los siguientes valores: {text_dic[list(text_dic.keys())[i]]}'
        sugerencia = yoga_assistant_response(sist_prompt_yoga, posture_data)
        dic_poses_resp[list(text_dic.keys())[i]] = sugerencia.choices[0].message.content
    
    return dic_poses_resp

