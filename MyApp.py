from math import pi, sin, cos


from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from direct.showbase.ShowBaseGlobal import globalClock
from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence
from panda3d.core import AntialiasAttrib
from panda3d.core import Point3
import math
from panda3d.core import PointLight

class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        #window
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)



        self.dayColors = [Vec4(0.8, 0.9, 1, 1), # midday
             Vec4(0.0549, 0.0980, 0.2588, 1)] # nighttime

        self.backgroundColor =Vec4(0.8, 0.9, 1, 1)
        self.lightPosition = Vec3(0,-1,-0.5)
        self.lightColor = Vec4(1,1,1,1)

        self.timeOfDay = 0



        self.directionalLight = DirectionalLight("directionalLight")
        self.directionalLight.setDirection(Vec3(0, 0, -1))
        self.directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLightNodePath = self.render.attachNewNode(self.directionalLight)
        self.render.setLight(directionalLightNodePath)



        house_light_1 = PointLight("House light 1")
        house_light_1.setColor((1,1,1,1))
        self.house_light_1_NodePath = self.render.attachNewNode(house_light_1)
        self.house_light_1_NodePath.setPos(-10,-10,10)
        self.render.setLight(self.house_light_1_NodePath)








        house_light_2 = PointLight("House light 2")
        house_light_2.setColor((1,1,1,1))
        self.house_light_2_NodePath = self.render.attachNewNode(house_light_2)
        self.house_light_2_NodePath.setHpr(-45, 45, 0)
        self.house_light_2_NodePath.setPos(5,5,2)
        self.render.setLight(self.house_light_2_NodePath)


        house_light_3 = PointLight("House light 3")
        house_light_3.setColor((1,1,1,1))
        self.house_light_3_NodePath = self.render.attachNewNode(house_light_3)
        self.house_light_3_NodePath.setHpr(-45, 45, 0)
        self.house_light_3_NodePath.setPos(5,-5,2)
        self.render.setLight(self.house_light_3_NodePath)





        self.render.setShaderAuto()

        # Load the environment model.

        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)





        #SKYCUBE WITH TEXTURES
        # self.cube = self.loader.loadCubeMap('cube_#.png')

        # self.spaceSkyBox = self.loader.loadModel('models/Cube.egg')
        # self.spaceSkyBox.setScale(1000)
        # self.spaceSkyBox.setBin('background', 0)
        # self.spaceSkyBox.setDepthWrite(0)
        # self.spaceSkyBox.setTwoSided(True)
        # self.spaceSkyBox.setTexture(self.cube, 1)
        # self.spaceSkyBox.reparentTo(self.render)




        # self.ball = self.loader.loadModel("models/Sphere_HighPoly.egg")
        # self.ball.setPos(-7, 0, 1)
        # self.ball.setScale(0.25)
        # self.ball.reparentTo(self.render)
        # self.tex = self.loader.loadCubeMap('enviromnent_cube_#.jpg')
        # self.ball.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeCubeMap)
        # self.ball.setTexture(self.tex)



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

        self.car_x = 7
        self.car_y = 0
        self.car_z = 0.55
        self.car = self.loader.loadModel('models/StationWagon/StationWagon.egg')
        self.car.setPos(self.car_x, self.car_y, self.car_z)
        self.car.setScale(0.25)

        self.car.reparentTo(self.render)


        #code for first person view
        self.disableMouse()

        self.cameraModel = self.loader.loadModel("models/camera")
        self.cameraModel.reparentTo(self.render)
        self.cameraModel.setPos(0, -20, 2)

        self.camera.reparentTo(self.cameraModel)


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
        self.taskMgr.add(self.updateLights, "updateLights")
        self.render.setAntialias(AntialiasAttrib.MAuto)
        carLight_r= PointLight("car light")
        self.carLight_r_Np = self.render.attachNewNode(carLight_r)
        self.carLight_r_Np.setPos(5.0,12.0, 1)
        self.carLight_r_Np.reparentTo(self.car)
        self.render.setLight(self.carLight_r_Np)

        carLight_l= PointLight("car light Left")
        self.carLight_l_Np = self.render.attachNewNode(carLight_l)
        self.carLight_l_Np.setPos(2.0,17.0, 1)
        self.carLight_l_Np.reparentTo(self.car)
        self.render.setLight(self.carLight_l_Np)


        self.moveCar()






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




    def updateLights(self, task):

        time_speed=0.001
        # Update the time of day
        self.timeOfDay += time_speed

        if self.timeOfDay>2:
            self.timeOfDay=0


        # Update the ambient light
        #self.ambientLight.setColor(self.dayColors[int(self.timeOfDay)])

        # Update the directional light
        if self.timeOfDay < 1:
            # Daytime to Nightime
            self.backgroundColor[0]-=0.7451 * time_speed
            self.backgroundColor[1]-=0.802 * time_speed
            self.backgroundColor[2]-=0.7412 * time_speed
            self.setBackgroundColor(self.backgroundColor)

            self.lightPosition[0]-=0.2*time_speed
            self.lightPosition[1]+=2*time_speed
            self.lightPosition[2]+=0.5*time_speed
            self.directionalLight.setDirection(self.lightPosition)

            if self.timeOfDay<0.5:
                self.lightColor[1]-=0.352*time_speed
                self.lightColor[2]-=1*time_speed
                self.directionalLight.setColor(self.lightColor)
            else:
                self.lightColor[0]-=0.8*time_speed
                self.lightColor[1]-=0.447*time_speed
                self.lightColor[2]+=0.2*time_speed
                self.directionalLight.setColor(self.lightColor)
        elif self.timeOfDay < 2:
            # Nighttime to Daytime
            self.backgroundColor[0]+=0.7451 * time_speed
            self.backgroundColor[1]+=0.802 * time_speed
            self.backgroundColor[2]+=0.7412 * time_speed
            self.setBackgroundColor(self.backgroundColor)


            self.lightPosition[0]+=0.2*time_speed
            self.lightPosition[1]-=2*time_speed
            self.lightPosition[2]-=0.5*time_speed
            self.directionalLight.setDirection(self.lightPosition)

            self.lightColor[0]+=0.8*time_speed
            self.lightColor[1]+=0.8*time_speed
            self.lightColor[2]+=0.8*time_speed
            self.directionalLight.setColor(self.lightColor)

        return Task.cont


    # def spinCameraTask(self, task):

    #     self.cameraRadius = 30.0

    #     angleDegrees = task.time * 60.0

    #     angleRadians = angleDegrees * (pi / 180.0)

    #     self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)

    #     self.camera.setHpr(angleDegrees, 0, 0)

    #     return Task.cont


    #Moving car
    def moveCar(self):
        
        posInterval1 = self.car.posInterval(3,

                                                   Point3(7.0, 7.0, 0.55),

                                                   startPos=Point3(7.0, -6.0, 0.55))

        posInterval2 = self.car.posInterval(3,

                                                   Point3(-7.0, 7.0, 0.55),

                                                   startPos=Point3(7.0, 7.0, 0.55))

        posInterval3 = self.car.posInterval(3,

                                                   Point3(-7.0, -6.0, 0.55),

                                                   startPos=Point3(-7.0, 7.0, 0.55))

        posInterval4 = self.car.posInterval(3,

                                                   Point3(7.0, -6.0, 0.55),

                                                   startPos=Point3(-7.0, -6.0, 0.55))


        hprInterval1 = self.car.hprInterval(3,

                                                   Point3(90, 0, 0),

                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.car.hprInterval(3,

                                                   Point3(180, 0, 0),

                                                   startHpr=Point3(90, 0, 0))
        hprInterval3 = self.car.hprInterval(3,

                                                   Point3(270, 0, 0),

                                                   startHpr=Point3(180, 0, 0))
        hprInterval4 = self.car.hprInterval(3,

                                                   Point3(360, 0, 0),

                                                   startHpr=Point3(270, 0, 0))



        # Create and play the sequence that coordinates the intervals.

        self.carPace = Sequence(posInterval1, hprInterval1,

                                  posInterval2, hprInterval2,

                                  posInterval3, hprInterval3,

                                  posInterval4, hprInterval4,

                                  name="carPace")

        self.carPace.loop()


app = MyApp()

app.run()
