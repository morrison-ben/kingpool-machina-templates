# {ai_context} This file implements the Google Vertex AI SDK connector with functions for text generation and embeddings.

import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingModel


DEFAULT_PROJECT = "prismatic-smoke-433121-j9"
DEFAULT_LOCATION = "us-central1"


def invoke_embedding(params):
    """
    Create embeddings using Google Vertex AI.
    
    :param params: Dictionary containing project, location, and model parameters
    :return: Embedding model instance or error message
    """
    project = params.get("project", DEFAULT_PROJECT)
    location = params.get("location", DEFAULT_LOCATION)
    model_name = params.get("model_name", "textembedding-gecko")

    try:
        # Initialize Vertex AI
        vertexai.init(project=project, location=location)
        
        # Create embedding model
        embedding_model = TextEmbeddingModel.from_pretrained(model_name)
        
        return {"status": True, "data": embedding_model, "message": "Model loaded."}

    except Exception as e:
        return {"status": "error", "message": f"Exception when creating model: {e}"}


def invoke_prompt(params):
    """
    Create a text generation model using Google Vertex AI Gemini.
    
    :param params: Dictionary containing project, location, and model parameters
    :return: Generation model instance or error message
    """
    project = params.get("project", DEFAULT_PROJECT)
    location = params.get("location", DEFAULT_LOCATION)
    model_name = params.get("model_name", "gemini-2.0-flash-001")
    
    try:
        # Initialize Vertex AI
        vertexai.init(project=project, location=location)
        
        # Create generative model
        model = GenerativeModel(model_name)
        
        return {"status": True, "data": model, "message": "Model loaded."}

    except Exception as e:
        return {"status": "error", "message": f"Exception when creating model: {e}"}


def invoke_vision(params):
    """
    Create a multimodal vision model using Google Vertex AI Gemini.
    
    :param params: Dictionary containing project, location, and model parameters
    :return: Vision model instance or error message
    """
    project = params.get("project", DEFAULT_PROJECT)
    location = params.get("location", DEFAULT_LOCATION)
    model_name = params.get("model_name", "gemini-2.0-flash-001")
    
    try:
        # Initialize Vertex AI
        vertexai.init(project=project, location=location)
        
        # Create vision model
        vision_model = GenerativeModel(model_name)
        
        return {"status": True, "data": vision_model, "message": "Model loaded."}

    except Exception as e:
        return {"status": "error", "message": f"Exception when creating model: {e}"} 