from math import pi, sin, cos


from direct.showbase.ShowBase import ShowBase
from panda3d.core import KeyboardButton
from direct.task import Task

from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence
from panda3d.core import WindowProperties
from panda3d.core import  AmbientLight, DirectionalLight
from panda3d.core import Vec4

class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        #window
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        #light 

        # mainLight = DirectionalLight("main light")
        # self.mainLightNodePath = self.render.attachNewNode(mainLight)
        # self.mainLightNodePath.setHpr(45, -45, 0)
        # self.render.setLight(self.mainLightNodePath)


        secondLight = DirectionalLight("Secondary light")
        self.secondLightNodePath = self.render.attachNewNode(secondLight)
        self.secondLightNodePath.setHpr(-45, 45, 0)
        self.secondLightNodePath.setPos(60,50,40)
        self.render.setLight(self.secondLightNodePath)


        # ambientLight = AmbientLight("ambient light")
        # ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        # self.ambientLightNodePath = self.render.attachNewNode(ambientLight)
        # self.render.setLight(self.ambientLightNodePath)
        

        self.render.setShaderAuto()

        # Load the environment model.

        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        #self.scene = self.loader.loadModel("models/house/new_house.obj")
        self.house = self.loader.loadModel("models/house/new_house.obj")

        # Reparent the model to render.

        #self.scene.reparentTo(self.render)

        # Apply scale and position transforms on the model.
        self.house.setScale(0.5, 0.5, 0.5)


        self.house.setPos(0, 0, 2.1)
        self.house.reparentTo(self.render)
        self.house.setHpr(self.house, 90)
        


        # Add the spinCameraTask procedure to the task manager.

        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")













        # Load and transform the panda actor.

        # self.wolfActor = Actor("models/lobo2/")
        # self.wolfActor.reparentTo(self.render)

        # self.wolfActor.play('Walk')
        # self.wolfActor.loop('Walk')
        # self.wolfActor.stop()
        #,

        #                         #{"walk": "models/panda-walk4"})

        # self.pandaActor.setScale(0.005, 0.005, 0.005)

        # self.pandaActor.reparentTo(self.render)

        # Loop its animation.

        #self.pandaActor.loop("walk")


        # Create the four lerp intervals needed for the panda to

        # walk back and forth.

        # posInterval1 = self.pandaActor.posInterval(13,

        #                                            Point3(0, -10, 0),

        #                                            startPos=Point3(0, 10, 0))

        # posInterval2 = self.pandaActor.posInterval(13,

        #                                            Point3(0, 10, 0),

        #                                            startPos=Point3(0, -10, 0))

        # hprInterval1 = self.pandaActor.hprInterval(3,

        #                                            Point3(180, 0, 0),

        #                                            startHpr=Point3(0, 0, 0))

        # hprInterval2 = self.pandaActor.hprInterval(3,

        #                                            Point3(0, 0, 0),

        #                                            startHpr=Point3(180, 0, 0))


        # # Create and play the sequence that coordinates the intervals.

        # self.pandaPace = Sequence(posInterval1, hprInterval1,

        #                           posInterval2, hprInterval2,

        #                           name="pandaPace")

        # self.pandaPace.loop()

    # Define a procedure to move the camera.

    def spinCameraTask(self, task):

        self.cameraRadius = 30.0

        angleDegrees = task.time * 60.0

        angleRadians = angleDegrees * (pi / 180.0)

        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)

        self.camera.setHpr(angleDegrees, 0, 0)


        #self.secondLightNodePath.setHpr(angleDegrees, 120, 120)

        return Task.cont



app = MyApp()

app.run()
