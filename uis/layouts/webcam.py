import gradio

from facefusion import state_manager
from facefusion.uis.components import about, age_modifier_options, execution, execution_thread_count, face_debugger_options, face_enhancer_options, face_swapper_options, frame_colorizer_options, frame_enhancer_options, lip_syncer_options, processors, source, webcam, webcam_options


def pre_check() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 4):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					processors.render()
				with gradio.Blocks():
					age_modifier_options.render()
				with gradio.Blocks():
					face_debugger_options.render()
				with gradio.Blocks():
					face_enhancer_options.render()
				with gradio.Blocks():
					face_swapper_options.render()
				with gradio.Blocks():
					frame_colorizer_options.render()
				with gradio.Blocks():
					frame_enhancer_options.render()
				with gradio.Blocks():
					lip_syncer_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
				with gradio.Blocks():
					webcam_options.render()
				with gradio.Blocks():
					source.render()
			with gradio.Column(scale = 11):
				with gradio.Blocks():
					webcam.render()
	return layout


def listen() -> None:
	processors.listen()
	age_modifier_options.listen()
	face_debugger_options.listen()
	face_enhancer_options.listen()
	face_swapper_options.listen()
	frame_colorizer_options.listen()
	frame_enhancer_options.listen()
	lip_syncer_options.listen()
	execution.listen()
	execution_thread_count.listen()
	source.listen()
	webcam.listen()


def run(ui : gradio.Blocks) -> None:
	ui.launch(favicon_path = 'facefusion.ico', inbrowser = state_manager.get_item('open_browser'))