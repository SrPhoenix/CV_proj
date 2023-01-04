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

        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = self.render.attachNewNode(mainLight)
        self.mainLightNodePath.setHpr(45, -45, 0)
        self.render.setLight(self.mainLightNodePath)


        secondLight = DirectionalLight("Secondary light")
        self.secondLightNodePath = self.render.attachNewNode(secondLight)
        self.secondLightNodePath.setHpr(-45, 45, 0)
        self.secondLightNodePath.setPos(60,50,40)
        self.render.setLight(self.secondLightNodePath)


        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(self.ambientLightNodePath)
        

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
        self.taskMgr.add(self.moveSun, "moveSun")


        self.car = self.loader.loadModel('models/StationWagon/StationWagon.egg')
        self.car.setPos(7, 0, 0.55)
        self.car.setScale(0.25)

        self.car.reparentTo(self.render)


        #code for first person view
        self.disableMouse()

        self.cameraModel = self.loader.loadModel("models/camera")
        self.cameraModel.reparentTo(self.render)
        self.cameraModel.setPos(0, -20, 2)

        self.camera.reparentTo(self.cameraModel)
        self.camera.setY(self.camera, 0)

		
        self.keyMap = {"w" : False, "s" : False, "a" : False, "d" : False, "space": False, "shift": False}

        self.accept("w", self.setKey, ["w", True])
        self.accept("s", self.setKey, ["s", True])	
        self.accept("a", self.setKey, ["a", True])	
        self.accept("d", self.setKey, ["d", True])

        self.accept("w-up", self.setKey, ["w", False])
        self.accept("s-up", self.setKey, ["s", False])
        self.accept("a-up", self.setKey, ["a", False])
        self.accept("d-up", self.setKey, ["d", False])
		
        self.accept("space", self.setKey, ["space", True])
        self.accept("space-up", self.setKey, ["space", False])

        self.accept("shift", self.setKey, ["shift", True])
        self.accept("shift-up", self.setKey, ["shift", False])



        self.taskMgr.add(self.cameraControl, "Camera Control")









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

    def setKey(self, key, value):
        self.keyMap[key] = value

    def cameraControl(self, task):
        dt = globalClock.getDt()
        if(dt > .20):
            return task.cont

        if(base.mouseWatcherNode.hasMouse() == True):
            mpos = base.mouseWatcherNode.getMouse()
            base.camera.setP(mpos.getY() * 30)
            base.camera.setH(mpos.getX() * -50)
            if (mpos.getX() < 0.1 and mpos.getX() > -0.1 ):
                self.cameraModel.setH(self.cameraModel.getH())
            else:
                self.cameraModel.setH(self.cameraModel.getH() + mpos.getX() * -1)
			
        if(self.keyMap["w"] == True):
            self.cameraModel.setY(self.cameraModel, 15 * dt)
            return task.cont
        elif(self.keyMap["s"] == True):
            self.cameraModel.setY(self.cameraModel, -15 * dt)
            return task.cont
        elif(self.keyMap["a"] == True):
            self.cameraModel.setX(self.cameraModel, -10 * dt)
            return task.cont
        elif(self.keyMap["d"] == True):
            self.cameraModel.setX(self.cameraModel, 10 * dt)
            return task.cont
        elif(self.keyMap["shift"] == True):
            self.cameraModel.setZ(self.cameraModel, -10 * dt)
            return task.cont
        elif(self.keyMap["space"] == True):
            self.cameraModel.setZ(self.cameraModel, 10 * dt)
            return task.cont
        else:
            return task.cont

    def moveSun(self, task):
        angleDegrees = task.time *20

        self.secondLightNodePath.setHpr(angleDegrees,0,0)

        return Task.cont

    # def spinCameraTask(self, task):

    #     self.cameraRadius = 30.0

    #     angleDegrees = task.time * 60.0

    #     angleRadians = angleDegrees * (pi / 180.0)

    #     self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)

    #     self.camera.setHpr(angleDegrees, 0, 0)

    #     return Task.cont



app = MyApp()

app.run()
