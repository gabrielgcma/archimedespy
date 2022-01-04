from os import replace, set_inheritable, setegid
from manim import *
import math

#version1

class Transformacoes(MovingCameraScene):
    def construct(self):

        # construindo as figuras
        circulo = Circle(radius=1, color=DARK_BLUE, stroke_width=1).scale(2)
        triangulo = Polygon([-1, -1.73, 0], [1, -1.73, 0], [0, 0, 0], color=ORANGE, stroke_width=1)

        raio = MathTex(r"raio = \frac{1}{2}").scale(0.2).shift([-1, -0.5, 0])
        raio2 = MathTex(r"raio = \frac{1}{2}").scale(0.2).shift([0, -1.85, 0])
        raios = VGroup(raio, raio2)
        
        r = MathTex(r"\frac{1}{2}").scale(0.3).shift([-0.5, -0.5, 0])
        r2 = Tex("2a").scale(0.3).shift([0, -1.90, 0])

        a = Tex("a").move_to([0.5, -1.9, 0]).scale(0.3).shift(RIGHT*0.01, UP*0.3)
        a2 = Tex("a").move_to([-0.5, -1.9, 0]).scale(0.3).shift(LEFT*0.01, UP*0.3)
        meios = VGroup(a, a2)

        angulo = Arc(start_angle=(4*PI)/3, angle=PI/3, radius=0.2, stroke_width=1)
        angulotexto = MathTex(r"2\theta").move_to(angulo).shift(DOWN*0.2).scale(0.3)
        angulodividido = MathTex(r"\theta").move_to(angulo).shift(LEFT*0.1, DOWN*0.16).scale(0.3)
        angulodividido2 = MathTex(r"\theta").move_to(angulo).shift(RIGHT*0.1, DOWN*0.16).scale(0.3)
        angulosd = VGroup(angulodividido, angulodividido2)

        linha = DashedLine(start=[0, 0, 0], end=[0, -1.73, 0], stroke_width=0.5)

        sen = Text("sen").scale(0.2).shift(DOWN*0.5, LEFT*1)
        theta = MathTex(r"\theta").next_to(sen, RIGHT*0.01).scale(0.3)
        sen2 = Text("=").scale(0.2).next_to(theta, RIGHT*0.35)
        sen3 = MathTex(r"\frac{a}{\frac{1}{2}}").next_to(sen2, RIGHT*0.001).scale(0.3)
        sen4 = MathTex('2a').next_to(sen2, RIGHT*0.01).scale(0.3)
        formulaseno = VGroup(sen, theta, sen2, sen3, sen4)
        formulaseno.shift(UP*0.3, LEFT*0.2)

        lado = Tex("lado do polígono").scale(0.22).move_to(sen).shift(LEFT*0.15)
        seno = Text("sen θ").scale(0.18).move_to(sen4).shift(UP*0.005)

        tequilatero = VGroup(triangulo, a, a2, linha, angulosd, angulo)

        ladoigualseno = VGroup(lado, seno, sen2)

        lados_polig = Text("número de lados do polígono = ").scale(0.7).shift(DOWN*3)
        lados_polig2 = Text("número de lados do polígono = ").scale(0.125).move_to([-1.5, 2.05, 0]) 

        seis = Integer(6).set_color(WHITE).scale(1).next_to(lados_polig, RIGHT*0.5)
        sete = Integer(7).set_color(WHITE).scale(1).next_to(lados_polig, RIGHT*0.5)
        oito = Integer(8).set_color(WHITE).scale(1).next_to(lados_polig, RIGHT*0.5)
        nove = Integer(9).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        dez = Integer(10).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        doze = Integer(12).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        quatorze = Integer(14).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        dezesseis = Integer(16).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        dezoito = Integer(18).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        vinte = Integer(20).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        trinta = Integer(30).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        quarenta = Integer(40).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        oitenta = Integer(80).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        centsessenta = Integer(160).set_color(WHITE).scale(1).next_to(lados_polig2, RIGHT*0.25)
        ene = Text("n").scale(1).next_to(lados_polig2, RIGHT*0.25)
        inf = Text("∞").scale(1).next_to(lados_polig2, RIGHT*0.25)

        hexagono = RegularPolygon(n=6, color=WHITE, stroke_width=1).scale(2)
        heptagono = RegularPolygon(n=7, color=WHITE, stroke_width=1).scale(1.95)
        octogono = RegularPolygon(n=8, color=WHITE, stroke_width=1).scale(2)
        eneagono = RegularPolygon(n=9, color=WHITE, stroke_width=1).scale(2)
        p10 = RegularPolygon(n=10, color=WHITE, stroke_width=1).scale(2)
        p12 = RegularPolygon(n=12, color=WHITE, stroke_width=1).scale(2)
        p14 = RegularPolygon(n=14, color=WHITE, stroke_width=1).scale(2)
        p16 = RegularPolygon(n=16, color=WHITE, stroke_width=1).scale(2)
        p18 = RegularPolygon(n=18, color=WHITE, stroke_width=1).scale(2)
        p20 = RegularPolygon(n=20, color=WHITE, stroke_width=1).scale(2)
        p30 = RegularPolygon(n=30, color=WHITE, stroke_width=1).scale(2)
        p40 = RegularPolygon(n=40, color=WHITE, stroke_width=1).scale(2)
        p80 = RegularPolygon(n=80, color=WHITE, stroke_width=1).scale(2)
        p160 = RegularPolygon(n=160, color=WHITE, stroke_width=1).scale(2)

        perimetro = Text("perímetro do polígono =").scale(0.3).shift(DOWN*3, LEFT*1.7)
        nlados = Text("número de lados").scale(0.3).next_to(perimetro, RIGHT*0.5)
        x = Text("x").scale(0.3).next_to(nlados, RIGHT*0.3)
        ladocomp = Text("tamanho dos lados").scale(0.3).next_to(x, RIGHT*0.5)
        n = Text("n").scale(0.3).move_to(nlados)
        sennovo = Text("sen θ").scale(0.3).move_to(ladocomp)
        sennovo2 = MathTex(r"sen(\frac{180^{\circ}}{n})").move_to(sennovo).scale(0.6)

        circseno = Circle(stroke_width=0.5, radius=0.5).move_to(sennovo)
        hexseno = RegularPolygon(n=6, stroke_width=0.5, radius=0.5).move_to(circseno)
        linhas1 = Line(start=[2.36, -2.57, 0], end=[2.85, -3.43, 0], stroke_width=0.5)
        linhas2 = Line(start=[2.36, -3.43, 0], end=[2.85, -2.57, 0], stroke_width=0.5)
        linhas3 = Line(start=[2.1, -3, 0], end=[3.1, -3, 0], stroke_width=0.5)
        angulomenor = Arc(start_angle=0, angle=2*PI, radius=0.08, stroke_width=0.35).move_to([2.605, -3, 0])
        angulomenort = Text("360º").next_to(angulomenor).scale(0.1).shift(LEFT*0.87, UP*0.1)
        linhatmenor = DashedLine(start=[2.605, -3, 0], end=[2.605, -3.43, 0], stroke_width=0.5)
        thetamenor = Text("θ").scale(0.1).next_to(linhatmenor, LEFT*0.05).shift(UP*0.1)
        thetamenor2 = Text("θ").scale(0.1).next_to(thetamenor, RIGHT*0.1)
        thetamenor3 = thetamenor2.copy().move_to([1.55, -2.5, 0]) 
        igual = Text("=").scale(0.1).move_to([1.65, -2.5, 0])
        anguloscontagem = Text("1").move_to([2.83, -2.8, 0]).scale(0.1).set_color(YELLOW)
        anguloscontagem2 = Text("2").move_to([2.605, -2.65, 0]).scale(0.1).set_color(YELLOW)
        anguloscontagem3 = Text("3").move_to([2.35, -2.8, 0]).scale(0.1).set_color(YELLOW)
        anguloscontagem4 = Text("4").move_to([2.35, -3.2, 0]).scale(0.1).set_color(YELLOW)
        anguloscontagem5 = Text("5").move_to([2.56, -3.3, 0]).scale(0.1).set_color(YELLOW)
        anguloscontagem6 = Text("6").move_to([2.83, -3.2, 0]).scale(0.1).set_color(YELLOW)

        divididopor = Line(stroke_width=0.5, start=([1.75, -2.51, 0]), end=([1.95, -2.51, 0]))
        divididopor2 = divididopor.copy().shift(DOWN*0.11)
        dois = Text("2").scale(0.1).move_to([1.85, -2.68, 0])
        tr60 = Text("360º").move_to([1.85, -2.45, 0]).scale(0.1)
        numerolados = Text("número de lados").scale(0.08).move_to([1.85, -2.57, 0])
        ene2 = Text("n").scale(0.1).move_to(numerolados)
        formulafinal = MathTex(r"\frac{180^{\circ}}{n}").scale(0.2).move_to(divididopor)

        formulamenor = VGroup(divididopor, divididopor2, dois, tr60, numerolados, ene2)

        circunf = Text('circunferência =').scale(0.2).move_to([-0.3, 0, 0])
        doispir = Text('2πr').scale(0.2).move_to([0.7, 0, 0])
        doispir2 = Text('2π(1/2)').scale(0.2).move_to(doispir)
        doispir3 = Text('π').scale(0.2).move_to(doispir)
        perim2 = Text('perímetro do polígono =').scale(0.2).move_to(circunf)
        pigual = Text('π =')
        enemaior = Text('n')
        formulaf1 = MathTex(r"perímetro=n{\cdot}sen(\frac{180^{\circ}}{n})").move_to([0, -3, 0]).scale(0.8)
        formulaf2 = MathTex(r"{\pi}=n{\cdot}sen(\frac{180^{\circ}}{n})").move_to([0, -3, 0])
        formulaf3 = MathTex(r"{\pi}=3{\cdot}sen(\frac{180^{\circ}}{3}").move_to([0, -3, 0])
        formulaf3r = MathTex(r"{\pi}=2.5980").move_to([0, -3, 0]) 
        formulaf6 = MathTex(r"{\pi}=6{\cdot}sen(\frac{180^{\circ}}{6})").move_to([0, -3, 0]) 
        formulaf6r = MathTex(r"{\pi}=3.0000").move_to([0, -3, 0])
        formulaf7 = MathTex(r"{\pi}=7{\cdot}sen(\frac{180^{\circ}}{7})").move_to([0, -3, 0])
        formulaf7r = MathTex(r"{\pi}=3.0371").move_to([0, -3, 0])
        formulaf8 = MathTex(r"{\pi}=8{\cdot}sen(\frac{180^{\circ}}{8})").move_to([0, -3, 0])
        formulaf8r = MathTex(r"{\pi}=3.0614").move_to([0, -3, 0])
        formulaf9 = MathTex(r"{\pi}=9{\cdot}sen(\frac{180^{\circ}}{9})").move_to([0, -3, 0])
        formulaf9r = MathTex(r"{\pi}=3.0781").move_to([0, -3, 0])
        formulaf10 = MathTex(r"{\pi}=10{\cdot}sen(\frac{180^{\circ}}{10})").move_to([0, -3, 0])
        formulaf10r = MathTex(r"{\pi}=3.0901").move_to([0, -3, 0])
        formulaf12 = MathTex(r"{\pi}=12{\cdot}sen(\frac{180^{\circ}}{12})").move_to([0, -3, 0])
        formulaf12r = MathTex(r"{\pi}=3.1058").move_to([0, -3, 0])
        formulaf14 = MathTex(r"{\pi}=14{\cdot}sen(\frac{180^{\circ}}{14})").move_to([0, -3, 0])
        formulaf14r = MathTex(r"{\pi}=3.1152").move_to([0, -3, 0])
        formulaf16 = MathTex(r"{\pi}=16{\cdot}sen(\frac{180^{\circ}}{16})").move_to([0, -3, 0])
        formulaf16r = MathTex(r"{\pi}=3.1214").move_to([0, -3, 0])
        formulaf18 = MathTex(r"{\pi}=18{\cdot}sen(\frac{180^{\circ}}{18})").move_to([0, -3, 0])
        formulaf18r = MathTex(r"{\pi}=3.1256").move_to([0, -3, 0])
        formulaf20 = MathTex(r"{\pi}=20{\cdot}sen(\frac{180^{\circ}}{20})").move_to([0, -3, 0])
        formulaf20r = MathTex(r"{\pi}=3.1286").move_to([0, -3, 0])
        formulaf30 = MathTex(r"{\pi}=30{\cdot}sen(\frac{180^{\circ}}{30})").move_to([0, -3, 0])
        formulaf30r = MathTex(r"{\pi}=3.1358").move_to([0, -3, 0])
        formulaf40 = MathTex(r"{\pi}=40{\cdot}sen(\frac{180^{\circ}}{40})").move_to([0, -3, 0])
        formulaf40r = MathTex(r"{\pi}=3.1383").move_to([0, -3, 0])
        formulaf80 = MathTex(r"{\pi}=80{\cdot}sen(\frac{180^{\circ}}{80})").move_to([0, -3, 0])
        formulaf80r = MathTex(r"{\pi}=3.140785261").move_to([0, -3, 0])
        formulaf160 = MathTex(r"{\pi}=160{\cdot}sen(\frac{180^{\circ}}{160})").move_to([0, -3, 0])
        formulaf160r = MathTex(r"{\pi}=3.141390794").move_to([0, -3, 0])
        formulaf320 = MathTex(r"{\pi}=320{\cdot}sen(\frac{180^{\circ}}{320})").move_to([0, -3, 0])
        formulaf320r = MathTex(r"{\pi}=3.141542188").move_to([0, -3, 0])
        formulaf640 = MathTex(r"{\pi}=640{\cdot}sen(\frac{180^{\circ}}{640})").move_to([0, -3, 0])
        formulaf640r = MathTex(r"{\pi}=3.141580037").move_to([0, -3, 0])   
        formulaf1280 = MathTex(r"{\pi}=1280{\cdot}sen(\frac{180^{\circ}}{1280})").move_to([0, -3, 0])
        formulaf1280r = MathTex(r"{\pi}=3.141589499").move_to([0, -3, 0])
        formulaf2560 = MathTex(r"{\pi}=2560{\cdot}sen(\frac{180^{\circ}}{2560})").move_to([0, -3, 0])
        formulaf2560r = MathTex(r"{\pi}=3.14159").move_to([0, -3, 0]).set_color(RED)

        # adicionando elementos
        #self.add(Axes().add_coordinates())
        self.play(GrowFromCenter(hexagono), Create(circulo), run_time=1)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=4).move_to([0, -1, 0]), run_time=0.4)
        self.play(Create(triangulo))
        self.play(FadeIn(raios), run_time=0.3)
        self.wait(0.5)
        self.play(Transform(raio, r), Transform(raio2, r2), run_time=0.6)
        self.play(Create(angulo), run_time=0.5)
        self.play(Create(angulotexto), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(angulotexto), run_time=0.3)
        self.play(Create(linha), run_time=0.3)
        self.play(FadeIn(angulosd), run_time=0.3)
        self.wait(0.5)
        self.play(Transform(mobject=r, target_mobject=a, replace_mobject_with_target_in_scene=True), 
            Transform(mobject=r2, target_mobject=a2, replace_mobject_with_target_in_scene=True), 
            run_time=0.4)
        self.play(FadeOut(raios), run_time=0.2)
        self.wait(0.5)
        self.play(Create(sen), Create(theta), Create(sen2), Create(sen3), run_time=0.3)
        self.wait(0.5)
        self.play(Transform(sen3, sen4, replace_mobject_with_target_in_scene=True), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(theta), run_time=0.3)
        self.play(Transform(sen, lado, replace_mobject_with_target_in_scene=True), run_time=0.5)
        self.play(Transform(sen4, seno, replace_mobject_with_target_in_scene=True), run_time=0.5)
        self.play(Restore(self.camera.frame), run_time=0.5) # saindo do zoom 
        self.play(FadeOut(tequilatero, ladoigualseno), run_time=0.5)

        # restaurar o zoom pro último camera frame state
        #self.play(Restore(self.camera.frame)) 

        self.play(Create(lados_polig), run_time=0.5)
        self.add(seis)
        self.play(Transform(mobject=hexagono, target_mobject=heptagono, replace_mobject_with_target_in_scene=True), 
            Transform(seis, sete, replace_mobject_with_target_in_scene=True), 
            run_time=0.5)
        self.wait(0.5)
        self.play(Transform(mobject=heptagono, target_mobject=octogono, replace_mobject_with_target_in_scene=True), 
            Transform(sete, oito, replace_mobject_with_target_in_scene=True), 
            run_time=0.5)
        self.wait(0.5)

        ## dando zoom
        self.camera.frame.save_state() # salva o estado atual da câmera
        self.play(self.camera.frame.animate.set(width=2.5).move_to([-1, 1.5, 0]), # seta o tamanho do zoom e o destino do zoom
            FadeOut(oito, lados_polig), 
            run_time=0.5) 
        self.wait(0.4)
        self.play(Create(lados_polig2), run_time=0.5)
        
        self.play(Transform(mobject=octogono, target_mobject=eneagono, replace_mobject_with_target_in_scene=True), Create(nove.scale(0.6)), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(mobject=eneagono, target_mobject=p10, replace_mobject_with_target_in_scene=True), 
                Transform(nove.scale(0.6), dez.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.5)
        self.play(Transform(mobject=p10, target_mobject=p12, replace_mobject_with_target_in_scene=True), 
                Transform(dez.scale(0.6), doze.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.5)
        self.play(Transform(mobject=p12, target_mobject=p14, replace_mobject_with_target_in_scene=True), 
                Transform(doze.scale(0.6), quatorze.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.5)
        self.play(Transform(mobject=p14, target_mobject=p16, replace_mobject_with_target_in_scene=True), 
                Transform(quatorze.scale(0.6), dezesseis.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.5)
        self.play(Transform(mobject=p16, target_mobject=p18, replace_mobject_with_target_in_scene=True), 
                Transform(dezesseis.scale(0.6), dezoito.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.play(Transform(mobject=p18, target_mobject=p20, replace_mobject_with_target_in_scene=True), 
                Transform(dezoito.scale(0.6), vinte.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.play(Transform(mobject=p20, target_mobject=p30, replace_mobject_with_target_in_scene=True), 
                Transform(vinte.scale(0.6), trinta.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.play(Transform(mobject=p30, target_mobject=p40, replace_mobject_with_target_in_scene=True), 
                Transform(trinta.scale(0.6), quarenta.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.play(Transform(mobject=p40, target_mobject=p80, replace_mobject_with_target_in_scene=True), 
                Transform(quarenta.scale(0.6), oitenta.scale(0.6), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.play(Transform(mobject=p80, target_mobject=p160, replace_mobject_with_target_in_scene=True), 
                Transform(oitenta.scale(0.6), centsessenta.scale(0.5), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.play(Transform(centsessenta.scale(0.5), inf.scale(0.5), replace_mobject_with_target_in_scene=True), 
                run_time=0.25)
        self.wait(0.5)
        self.play(Restore(self.camera.frame), FadeOut(lados_polig2, inf))
        self.wait(0.5)
        self.play(Create(perimetro), Create(nlados), Create(x), Create(ladocomp), run_time=0.5)
        self.wait(0.3)
        self.play(Transform(nlados, n, replace_mobject_with_target_in_scene=True), 
                Transform(ladocomp, sennovo, replace_mobject_with_target_in_scene=True), run_time=0.5)
        self.wait()
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=2.5).move_to(sennovo), run_time=0.5)
        self.play(Transform(sennovo, circseno, replace_mobject_with_target_in_scene=True), 
                Create(hexseno), run_time=0.5)
        self.play(Create(linhas1), Create(linhas2), Create(linhas3), Create(angulomenor))
        self.play(Create(angulomenort), run_time=0.5)
        self.play(Create(linhatmenor), Create(thetamenor), Create(thetamenor2), run_time=0.5)
        self.play(Transform(thetamenor, thetamenor3, replace_mobject_with_target_in_scene=False), 
                Transform(thetamenor2, thetamenor3, replace_mobject_with_target_in_scene=False))
        self.play(Create(igual), Create(tr60), Create(divididopor), 
                Create(divididopor2), Create(dois), run_time=0.2)
        self.play(Create(anguloscontagem), run_time=0.2)
        self.play(Create(anguloscontagem2), run_time=0.2)
        self.play(Create(anguloscontagem3), run_time=0.2)
        self.play(Create(anguloscontagem4), run_time=0.2)
        self.play(Create(anguloscontagem5), run_time=0.2)
        self.play(Create(anguloscontagem6), run_time=0.2)
        self.wait(0.25)
        self.play(Transform(anguloscontagem, numerolados, replace_mobject_with_target_in_scene=True), 
                Transform(anguloscontagem2, numerolados, replace_mobject_with_target_in_scene=True), 
                Transform(anguloscontagem3, numerolados, replace_mobject_with_target_in_scene=True), 
                Transform(anguloscontagem4, numerolados, replace_mobject_with_target_in_scene=True), 
                Transform(anguloscontagem5, numerolados, replace_mobject_with_target_in_scene=True), 
                Transform(anguloscontagem6, numerolados, replace_mobject_with_target_in_scene=True), 
                run_time=0.5)
        self.wait(0.3)
        self.play(Transform(numerolados, ene2, replace_mobject_with_target_in_scene=True), run_time=0.5)
        self.wait(1)
        self.play(Transform(formulamenor, formulafinal, replace_mobject_with_target_in_scene=True), 
            run_time=0.5)
        self.wait(1)
        self.play(Restore(self.camera.frame), ReplacementTransform(thetamenor2, sennovo2), 
            ReplacementTransform(thetamenor, sennovo2), ReplacementTransform(thetamenor3, sennovo2),
            ReplacementTransform(igual, sennovo2), ReplacementTransform(formulafinal, sennovo2), 
            ReplacementTransform(linhas1, sennovo2), ReplacementTransform(linhas2, sennovo2), 
            ReplacementTransform(linhas3, sennovo2), ReplacementTransform(angulomenor, sennovo2), 
            ReplacementTransform(angulomenort, sennovo2), ReplacementTransform(linhatmenor, sennovo2), 
            ReplacementTransform(circseno, sennovo2), ReplacementTransform(hexseno, sennovo2), 
            run_time=0.5)
        self.camera.frame.save_state()
        self.wait(0.5)
        self.play(self.camera.frame.animate.set(width=3).move_to(ORIGIN), Create(circunf), Create(doispir), run_time=0.5)
        self.wait(0.4)
        self.play(ReplacementTransform(doispir, doispir2), run_time=0.5)
        self.play(ReplacementTransform(doispir2, doispir3), run_time=0.5)
        self.play(ReplacementTransform(circunf, perim2), run_time=0.5)
        self.wait(0.3)
        self.play(Restore(self.camera.frame), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(perimetro), 
            FadeOut(n), 
            FadeOut(x), 
            FadeOut(sennovo2), 
            FadeOut(perim2), 
            FadeOut(doispir3), 
            run_time=0.3)
        self.play(Create(formulaf1), run_time=0.5)
        self.wait(0.5)
        self.play(Create(formulaf2), FadeOut(formulaf1), run_time=0.5)
        self.play(FadeOut(p160))
        self.play(GrowFromCenter(hexagono), ReplacementTransform(formulaf2, formulaf6), run_time=0.8)
        self.play(ReplacementTransform(formulaf6, formulaf6r), run_time=0.5)
        self.wait(0.5)
        self.play(ReplacementTransform(hexagono, heptagono), 
            ReplacementTransform(formulaf6r, formulaf7), 
            run_time=0.5)
        self.play(ReplacementTransform(formulaf7, formulaf7r), run_time=0.5)
        self.wait(0.5)
        self.play(ReplacementTransform(heptagono, octogono), 
            ReplacementTransform(formulaf7r, formulaf8), 
            run_time=0.5)
        self.play(ReplacementTransform(formulaf8, formulaf8r), run_time=0.5)
        self.wait(0.5)
        self.play(ReplacementTransform(octogono, eneagono), 
            ReplacementTransform(formulaf8r, formulaf9), 
            run_time=0.5)
        self.play(ReplacementTransform(formulaf9, formulaf9r), run_time=0.5)
        self.play(ReplacementTransform(eneagono, p10), 
            ReplacementTransform(formulaf9r, formulaf10), 
            run_time=0.5)
        self.play(ReplacementTransform(formulaf10, formulaf10r), run_time=0.5)
        self.play(ReplacementTransform(p10, p12), ReplacementTransform(formulaf10r, formulaf12), run_time=0.5)
        self.play(ReplacementTransform(formulaf12, formulaf12r), run_time=0.5)
        self.play(ReplacementTransform(p12, p14), ReplacementTransform(formulaf12r, formulaf14), run_time=0.25)
        self.play(ReplacementTransform(formulaf14, formulaf14r), run_time=0.25)
        self.play(ReplacementTransform(p14, p16), ReplacementTransform(formulaf14r, formulaf16), run_time=0.25)
        self.play(ReplacementTransform(formulaf16, formulaf16r), run_time=0.25)
        self.play(ReplacementTransform(p16, p18), ReplacementTransform(formulaf16r, formulaf18), run_time=0.15)
        self.play(ReplacementTransform(formulaf18, formulaf18r), run_time=0.15)
        self.play(ReplacementTransform(p18, p20), ReplacementTransform(formulaf18r, formulaf20), run_time=0.15)
        self.play(ReplacementTransform(formulaf20, formulaf20r), run_time=0.15)
        self.play(ReplacementTransform(p20, p30), ReplacementTransform(formulaf20r, formulaf30), run_time=0.15)
        self.play(ReplacementTransform(formulaf30, formulaf30r), run_time=0.15)
        self.play(ReplacementTransform(p30, p40), ReplacementTransform(formulaf30r, formulaf40), run_time=0.15)
        self.play(ReplacementTransform(formulaf40, formulaf40r), run_time=0.15)
        self.play(ReplacementTransform(p40, p80), ReplacementTransform(formulaf40r, formulaf80), run_time=0.15)
        self.play(ReplacementTransform(formulaf80, formulaf80r), run_time=0.15)
        self.play(ReplacementTransform(p80, p160), ReplacementTransform(formulaf80r, formulaf160), run_time=0.15)
        self.play(ReplacementTransform(formulaf160, formulaf160r), run_time=0.075)
        self.play(ReplacementTransform(formulaf160r, formulaf320), run_time=0.075)
        self.play(ReplacementTransform(formulaf320, formulaf320r), run_time=0.075)
        self.play(ReplacementTransform(formulaf320r, formulaf640), run_time=0.075)
        self.play(ReplacementTransform(formulaf640, formulaf640r), run_time=0.075)
        self.play(ReplacementTransform(formulaf640r, formulaf1280), run_time=0.075)
        self.play(ReplacementTransform(formulaf1280, formulaf1280r), run_time=0.075)
        self.play(ReplacementTransform(formulaf1280r, formulaf2560), run_time=0.075)
        self.play(ReplacementTransform(formulaf2560, formulaf2560r), run_time=0.075)
        self.wait(2)
