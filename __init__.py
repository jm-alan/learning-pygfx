from PySide6 import QtWidgets
from wgpu.gui.qt import WgpuCanvas
import pygfx

app = QtWidgets.QApplication([])

# Create a canvas and a renderer
canvas = WgpuCanvas()
renderer = pygfx.renderers.WgpuRenderer(canvas)

# Populate a scene with a cube
scene = pygfx.Scene()
geometry = pygfx.box_geometry(200, 200, 200)
material = pygfx.MeshPhongMaterial(color=(1, 1, 0, 1))
cube = pygfx.Mesh(geometry, material)
scene.add(cube)

camera = pygfx.PerspectiveCamera(70, 16 / 9)
camera.position.z = 400

def animate():
  rot = pygfx.linalg.Quaternion().set_from_euler(pygfx.linalg.Euler(0.005, 0.01))
  cube.rotation.multiply(rot)

  renderer.render(scene, camera)
  canvas.request_draw()

canvas.request_draw(animate)
app.exec()
