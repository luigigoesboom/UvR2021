
import unittest


poti_s_slike = [
    (0, 6, ">^^>^>>vv>^>>v>"),  # rdeči
    (2, 4, ">>vv<<^"),  # zeleni
    (5, 3, ">vv<v<^<vv>>"),  # modri
    (8, 8, "^^^^<<^^<<<<<"),  # oranžni
]


class Test06(unittest.TestCase):
    def test_01_koraki(self):
        self.assertEqual(
            [(0, 6), (1, 6), (1, 5), (1, 4), (2, 4), (2, 3), (3, 3), (4, 3),
             (4, 4), (4, 5), (5, 5), (5, 4), (6, 4), (7, 4), (7, 5), (8, 5)],
            koraki(*poti_s_slike[0]))  # rdeča pot
        self.assertEqual(
            [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (3, 6), (2, 6), (2, 5)],
            koraki(*poti_s_slike[1]))  # zelena pot
        self.assertEqual(
            [(5, 3), (6, 3), (6, 4), (6, 5), (5, 5), (5, 6), (4, 6), (4, 5),
             (3, 5), (3, 6), (3, 7), (4, 7), (5, 7)],
            koraki(*poti_s_slike[2]))  # modra pot
        self.assertEqual(
            [(8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (7, 4), (6, 4),
             (6, 3), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2), (1, 2)],
            koraki(*poti_s_slike[3]))  # oranzna pot

        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1),
             (2, 1), (3, 1), (3, 2), (3, 3), (3, 2), (2, 2)],
            koraki(0, 0, "vv>>>^<>vv^<"))
        self.assertEqual(
            [(10, 80), (10, 81), (10, 82), (11, 82), (12, 82), (13, 82),
             (13, 81), (12, 81), (13, 81), (13, 82), (13, 83), (13, 82),
             (12, 82)],
            koraki(10, 80, "vv>>>^<>vv^<"))
        self.assertEqual([(4, 8)], koraki(4, 8, ""))

    def test_02_cilj(self):
        self.assertEqual((8, 5), cilj(*poti_s_slike[0]))
        self.assertEqual((2, 5), cilj(*poti_s_slike[1]))
        self.assertEqual((5, 7), cilj(*poti_s_slike[2]))
        self.assertEqual((1, 2), cilj(*poti_s_slike[3]))
        self.assertEqual((2, 2), cilj(0, 0, "vv>>>^<>vv^<"))
        self.assertEqual((12, 82), cilj(10, 80, "vv>>>^<>vv^<"))
        self.assertEqual((4, 8), cilj(4, 8, ""))

    def test_03_cilji(self):
        self.assertEqual([(8, 5), (2, 5), (5, 7), (1, 2)], cilji(poti_s_slike))
        self.assertEqual(
            [(2, 2), (12, 82), (4, 8)],
            cilji([(0, 0, "vv>>>^<>vv^<"),
                   (10, 80, "vv>>>^<>vv^<"),
                   (4, 8, "")]))

        self.assertEqual(
            [(1, 7), (2, 3), (5, 5)],
            cilji([(3, 6, "<<v"), (2, 1, "vv"), (5, 5, "")]))

    def test_04_obiskana(self):
        self.assertEqual(
            {(4, 4), (4, 3), (4, 2), (5, 2), (5, 3), (5, 4), (3, 4)},
            obiskana(4, 4, "^^>vv<<")
        )
        self.assertEqual(
            {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1),
             (2, 1), (3, 1), (3, 3)},
            obiskana(0, 0, "vv>>>^<>vv^<")
        )

    def test_05_najveckrat_obiskana(self):
        self.assertEqual(
            {(2, 2)},
            najveckrat_obiskana([(0, 0, "vv>>>^<>vv^<"),
                                 (2, 2, "^"),
                                 (1, 1, "v>^")]))
        self.assertEqual(
            {(3, 2)},
            najveckrat_obiskana([(0, 0, "vv>>>^<>vv^<"),
                                 (1, 1, "v>^"),
                                 (3, 2, "")]))
        self.assertEqual(
            {(0, 0), (1, 0), (2, 0), (3, 0)},
            najveckrat_obiskana([(0, 0, ">>>"), (0, 0, ">>>"), (0, 0, ">>>"), (0, 0, ">>>>")]))
        self.assertEqual(
            {(2, 0)},
            najveckrat_obiskana([(0, 0, ">>>"), (0, 0, ">>>"), (0, 0, ">>>"), (0, 0, ">>><")]))
        self.assertEqual({(4, 5), (6, 4)}, najveckrat_obiskana(poti_s_slike))


def strip_ani(s):
    return ["".join(v.rstrip(" ") for v in x.strip()) for x in s]


class Test07(unittest.TestCase):
    def test_01_situacija(self):
        e = set()

        self.assertEqual([[e, e, e, e], [e, e, e, e]], situacija([], [], 4, 2))
        self.assertEqual([[e, {"a"}, e, e], [{"A"}, e, e, e]],
                         situacija([(0, 1)], [(1, 0)], 4, 2))

        self.assertEqual(
            [[e, {'A'}, e, e],
             [e, {'d'}, e, {'C', 'c', 'b'}],
             [{'D', 'B'}, e, {'a'}, e]],
            situacija([(1, 0), (0, 2), (3, 1), (0, 2)],
                      [(2, 2), (3, 1), (3, 1), (1, 1)], 4, 3)
        )

    def test_02_znak(self):
        self.assertEqual(".", znak(set()))
        self.assertEqual("F", znak({"F"}))
        self.assertEqual("b", znak({"b"}))
        self.assertEqual("3", znak({"b", "A", "t"}))
        self.assertEqual("5", znak({"b", "A", "t", "r", "Z"}))

        m = {"F"}
        self.assertEqual("F", znak({"F"}))
        self.assertEqual({"F"}, m)

    def test_03_izris(self):
        e = set()
        self.assertEqual("""
.A..
.d.3
2.a.
""".strip(), izris([[e, {'A'}, e, e],
                    [e, {'d'}, e, {'C',  'c', 'b'}],
                    [{'D', 'B'}, e, {'a'}, e]])
                         )

    def test_04_animacija0(self):
        self.assertEqual(strip_ani([
            """
            ......
            ..A...
            ......
            ......
            ......
            ......
            """,
            """
            ......
            ......
            ..A...
            ......
            ......
            ......
            """,
            """
            ......
            ......
            ......
            ..A...
            ......
            ......
            """,
            """
            ......
            ......
            ......
            ...A..
            ......
            ......
            """,
            """
            ......
            ......
            ......
            ....A.
            ......
            ......
            """,
            """
            ......
            ......
            ......
            .....A
            ......
            ......
            """,
            """
            ......
            ......
            .....A
            ......
            ......
            ......
            """,
            """
            ......
            ......
            ....A.
            ......
            ......
            ......
            """,
            """
            ......
            ......
            .....A
            ......
            ......
            ......
            """,
            """
            ......
            ......
            ......
            .....A
            ......
            ......
            """,
            """
            ......
            ......
            ......
            ......
            .....A
            ......
            """,
            """
            ......
            ......
            ......
            .....A
            ......
            ......
            """,
            """
            ......
            ......
            ......
            ....A.
            ......
            ......
            """]), animacija0(2, 1, "vv>>>^<>vv^<", 6, 6))


class Test08(unittest.TestCase):
    def test_01_dopolnjeno(self):
        s = ["Ana", "Berta"]
        self.assertEqual(["Ana"] + ["Berta"] * 20, dopolnjeno(s, 21))
        self.assertEqual(["Ana", "Berta"], s)

        s = [(1, 5), (1, 6), (2, 6), (3, 6)]
        self.assertEqual([(1, 5), (1, 6), (2, 6), (3, 6), (3, 6), (3, 6), (3, 6)],
                         dopolnjeno(s, 7))
        self.assertEqual([(1, 5), (1, 6), (2, 6), (3, 6)], s)

    def test_02_razporedi(self):
        self.assertEqual(
            ([[(0, 2), (3, 3), (4, 2)],
              [(1, 2), (2, 3), (4, 2)],
              [(2, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)]],
             [[(1, 2), (1, 1)],
              [(1, 1), (2, 1)],
              [(1, 0), (3, 1)],
              [(0, 0), (3, 1)],
              [(1, 0), (3, 1)],
              [(2, 0), (3, 1)]]),
            razporedi([(0, 2, ">>>"), (3, 3, "<v"), (4, 2, "")],
                      [(1, 2, "^^<>>"), (1, 1, ">>")]))
        self.assertEqual(
            ([[(1, 2), (1, 1)],
              [(1, 1), (2, 1)],
              [(1, 0), (3, 1)],
              [(0, 0), (3, 1)],
              [(1, 0), (3, 1)],
              [(2, 0), (3, 1)]],
             [[(0, 2), (3, 3), (4, 2)],
              [(1, 2), (2, 3), (4, 2)],
              [(2, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)]]),
            razporedi([(1, 2, "^^<>>"), (1, 1, ">>")],
                      [(0, 2, ">>>"), (3, 3, "<v"), (4, 2, "")],
                      ))
        self.assertEqual(
            ([[(0, 2), (3, 3), (4, 2)],
              [(1, 2), (2, 3), (4, 2)],
              [(2, 2), (2, 4), (4, 2)],
              [(3, 2), (2, 4), (4, 2)]],
             []),
            razporedi([(0, 2, ">>>"), (3, 3, "<v"), (4, 2, "")], []))
        self.assertEqual(
            ([],
             [[(1, 2), (1, 1)],
              [(1, 1), (2, 1)],
              [(1, 0), (3, 1)],
              [(0, 0), (3, 1)],
              [(1, 0), (3, 1)],
              [(2, 0), (3, 1)]]),
            razporedi([], [(1, 2, "^^<>>"), (1, 1, ">>")]))
        self.assertEqual(
            ([], [[(1, 2),]]),
            razporedi([], [[1, 2, ""]]))
        self.assertEqual(([], []), razporedi([], []))


    def test_03_animacija(self):
        self.assertEqual(strip_ani([
            """
            .....
            .b...
            Aa..C
            ...B.
            .....
            """,
            """
            .....
            .ab..
            .A..C
            ..B..
            .....
            """,
            """
            .a...
            ...b.
            ..A.C
            .....
            ..B..
            """,
            """
            a....
            ...b.
            ...AC
            .....
            ..B..
            """,
            """
            .a...
            ...b.
            ...AC
            .....
            ..B..
            """,
            """
            ..a..
            ...b.
            ...AC
            .....
            ..B..
            """]),
            animacija([(0, 2, ">>>"), (3, 3, "<v"), (4, 2, "")],
                      [(1, 2, "^^<>>"), (1, 1, ">>")], 5, 5)
        )
        self.assertEqual(strip_ani([
            """
            .....
            .b.D.
            Aa..C
            ...B.
            ...c.
            """,
            """
            .....
            .abD.
            .A..C
            ..Bc.
            .....
            """,
            """
            .a...
            ...2.
            ..AcC
            .....
            ..B..
            """,
            """
            a....
            ...3.
            ...AC
            .....
            ..B..
            """,
            """
            .a.c.
            ...2.
            ...AC
            .....
            ..B..
            """,
            """
            ..ac.
            ...2.
            ...AC
            .....
            ..B..
            """]),
            animacija([(0, 2, ">>>"), (3, 3, "<v"), (4, 2, ""), (3, 1, "")],
                      [(1, 2, "^^<>>"), (1, 1, ">>"), (3, 4, "^^^^")], 5, 5)
        )

    def test_04_prvo_srecanje(self):
        self.assertEqual(
            (3, 2),
            prvo_srecanje((1, 4, "^^>>v<v<"),
                          (1, 2, ">^>vvv<>")))
        self.assertEqual(
            (3, 2),
            prvo_srecanje((1, 4, "^^>>v<v<"),
                          (2, 2, ">")))
        self.assertIsNone(
            prvo_srecanje((1, 4, "^^>>v<v<"),
                          (5, 0, ">>>>>")))
        self.assertIsNone(
            prvo_srecanje((1, 1, ">>>>>"),
                          (2, 1, ">>>>>")))
        self.assertEqual(
            (4, 1),
            prvo_srecanje((2, 1, ">>"),
                          (1, 1, ">>>>>>")))

    def test_05_bingo(self):
        self.assertEqual(
            (13, 14),
            bingo([(10, 14, ">>>>>>>>")],
                  (12, 16, "^>^>^>^>^>")))
        self.assertEqual(
            (14, 13),
            bingo([(9, 13, ">>>>>>>>")],
                  (12, 16, "^>^>^>^>^>")))
        self.assertEqual(
            (15, 12),
            bingo([(8, 12, ">>>>>>>>")],
                  (12, 16, "^>^>^>^>^>")))
        self.assertEqual(
            (13, 14),
            bingo([(8, 12, ">>>>>>>>"), (10, 14, ">>>>>>>>"), (9, 13, ">>>>>>>>")],
                  (12, 16, "^>^>^>^>^>")))


class Test09(unittest.TestCase):
    def test_simulacija(self):
        # V tem bloku je ugrabljenec na (2, 2), marsovci pa na različnih lokacijah

        # Marsovec je na (2, 2); prideta dva specialca, eden zgrabi marsovca, drugi ugrabljenca
        self.assertTrue(simulacija([">>vv", ">>vv"], [(2, 2, "")]))

        # Specialec pobere marsovca, manjka pa specialec, ki reši ugrabljenca
        self.assertFalse(simulacija([">>vv"], [(2, 2, "")]))

        # Marsovca sta na koncu na (2, 2) in (1, 2)
        self.assertTrue(simulacija([">>vv", ">vv", ">>vv"], [(2, 0, "vv"), (3, 2, "<<")]))

        # Marsovca sta na koncu na (2, 2) in (1, 2)
        # Specialca pobereta marsovca, manjka pa specialec, ki reši ugrabljenca
        self.assertFalse(simulacija([">>vv", ">vv"], [(2, 0, "vv"), (3, 2, "<<")]))

        # Marsovca sta na koncu na (2, 3) in (1, 2)! Tega na (2, 3) ne ulovimo.
        self.assertFalse(simulacija([">>vv", ">vv", ">>vv"], [(2, 0, "vvv"), (3, 2, "<<")]))

        # Zdaj pa ga
        self.assertTrue(simulacija([">>vv", ">vv", ">>vvv"], [(2, 0, "vvv"), (3, 2, "<<")]))

        # En specialec preveč; nič hudega
        self.assertTrue(simulacija([">>vv", ">vv", "vv", ">>vvv"], [(2, 0, "vvv"), (3, 2, "<<")]))

        # Marsovca končata na (3, 2) in (1, 2)
        # Ugrabljenec sta lahko na (2, 2) ali (3, 2); enega ne dobimo
        self.assertFalse(simulacija([">>vv", ">vv", ">>>>v"], [(2, 0, "vv>"), (3, 2, "<<")]))
        self.assertFalse(simulacija([">>>>v", ">vv", ">>>>v"], [(2, 0, "vv>"), (3, 2, "<<")]))

        # Zdaj je pa v redu
        self.assertTrue(simulacija([">>vv", ">vv", "vv>>>", "vv>>>"], [(2, 0, "vv>"), (3, 2, "<<")]))

        # S slike
        self.assertTrue(
            simulacija(["vvv>>",  # rdeči
                        ">>>>>vvvv>",  # desni ugrabljenec
                        ">>>>vvvvvvv",  # modri
                        ">>vvvvv",  # zeleni
                        ">vv",  # oranžni
                        "v>>>>vvvv"  # levi ugrabljenec
                        ],
                       poti_s_slike)
        )

        # Ta, ki je bil planiran za zelenega, prej naleti na rdečega
        # pazi na vrstni red!
        self.assertFalse(
            simulacija([">>>>>vvvv>",  # desni ugrabljenec
                        ">>>>vvvvvvv",  # modri
                        ">>vvvvv",  # zeleni
                        ">vv",  # oranžni
                        "vvv>>",  # rdeči
                        "v>>>>vvvv"  # levi ugrabljenec
                        ],
                       poti_s_slike)
        )

        # Zgrešimo levega ugrabljenca
        self.assertFalse(
            simulacija(["vvv>>",  # rdeči
                        ">>>>>vvvv>",  # desni ugrabljenec
                        ">>>>vvvvvvv",  # modri
                        ">>vvvvv",  # zeleni
                        ">vv",  # oranžni
                        "v>>>>vvvvv"  # levi ugrabljenec
                        ],
                       poti_s_slike)
        )

        # Zgrešimo desnega ugrabljenca
        self.assertFalse(
            simulacija(["vvv>>",  # rdeči
                        ">>>>>vvvv",  # desni ugrabljenec
                        ">>>>vvvvvvv",  # modri
                        ">>vvvvv",  # zeleni
                        ">vv",  # oranžni
                        "v>>>>vvvvv"  # levi ugrabljenec
                        ],
                       poti_s_slike)
        )

        # S slike - s podaljšanimi potmi tistih, ki se v resnici
        # prej primejo marsovca
        self.assertTrue(
            simulacija(["vvv>>>>v>>vv<",  # rdeči
                        ">>>>>vvvv>",  # desni ugrabljenec
                        ">>>>vvvvvvv>>v<<>>",  # modri
                        ">>vvvvv^^^<<",  # zeleni
                        ">vv^^v>v",  # oranžni
                        "v>>>>vvvv"  # levi ugrabljenec
                        ],
                       poti_s_slike)
        )


class Test10(unittest.TestCase):
    def test_strategija(self):
        specialci = strategija(poti_s_slike)
        self.assertTrue(simulacija(specialci, poti_s_slike))
        self.assertEqual(10, max(len(p) for p in specialci))

        marsovci = [(2, 0, "vv>>"), (3, 0, "vvv"), (0, 1, ">>>>")]
        specialci = strategija(marsovci)
        self.assertTrue(simulacija(specialci, marsovci))
        self.assertEqual(6, len(specialci))
        self.assertEqual(6, max(len(p) for p in specialci))

        marsovci = [(4, 2, "<<^^"), (4, 1, "<<<<"), (3, 3, "^^^")]
        specialci = strategija(marsovci)
        self.assertTrue(simulacija(specialci, marsovci))
        self.assertEqual(6, len(specialci))
        self.assertEqual(5, max(len(p) for p in specialci))

        marsovci = [(1, 2, "^^>>>"), (2, 2, "^<<vv")]
        specialci = strategija(marsovci)
        self.assertTrue(simulacija(specialci, marsovci))
        self.assertEqual(3, len(specialci))
        self.assertEqual(2, max(len(p) for p in specialci))

        marsovci = [(4, 0, "<<<vv"), (0, 3, "^^>>v")]
        specialci = strategija(marsovci)
        self.assertTrue(simulacija(specialci, marsovci))
        self.assertEqual(3, len(specialci))
        self.assertEqual(2, max(len(p) for p in specialci))

        marsovci = [(0, 0, "")]
        self.assertEqual(["", ""], strategija(marsovci))

        marsovci = [(4, 0, "<<<vv"), (0, 3, "^^>>v"), (1000, 1000, ">" * 1000)]
        specialci = strategija(marsovci)
        self.assertTrue(simulacija(specialci, marsovci))
        self.assertEqual(4, len(specialci))
        self.assertEqual(3000, max(len(p) for p in specialci))


if __name__ == "__main__":
    unittest.main()
