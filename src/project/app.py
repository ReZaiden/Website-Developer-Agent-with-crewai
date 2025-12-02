from project.crew import Project
import gradio as gr

if __name__ == '__main__':
    def run_agent(requirements: str, module_name: str, class_name: str) -> str:
        result = Project().crew().kickoff({'requirements': requirements, 'module_name': module_name, 'class_name': class_name})
        return result.raw

    iface = gr.Interface(
        fn=run_agent,
        inputs=[
            gr.Textbox(label="requirements", placeholder="describe the program"),
            gr.Textbox(label="module_name", placeholder="module name"),
            gr.Textbox(label="class_name", placeholder="class name for module")
        ],
        outputs=gr.Textbox(label="Output"),
        title="Three Fields Example"
    )

    iface.launch(server_port=11228)
