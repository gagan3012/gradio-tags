
import gradio as gr
from gradio_tags import tags


example = tags().example_inputs()

demo = gr.Interface(
    lambda x:x,
    tags(),  # interactive version of your component
    tags(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
