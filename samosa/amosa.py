from point import Point
import random
import math


def amosa_select(archive, cur_point, new_point, temp):
    dominance = Point.pareto_dominance(new_point, cur_point)
    case = 0
    if dominance > 0:  # Case 1 cur_point dominates new_point
        case = 1
        deldom = archive.calculate_dom(new_point, cur_point)
        k = 1
        for point in archive.points:
            if point != cur_point:
                if Point.pareto_dominance(new_point, point) > 0:
                    deldom = deldom + archive.calculate_dom(new_point, point)
                    k = k + 1
        deldom_avg = deldom / k
        e = float()
        try:
            e = math.exp(deldom_avg / temp)
        except OverflowError:
            e = math.inf
        prob = 1.0 / (1.0 + e)
        if random.random() <= prob:
            cur_point = new_point

    elif dominance == 0:  # Case 2 new_point and cur_point non-dominating
        case = 2
        k1 = 0
        k2 = 0
        k3 = 0
        dominated_points = []
        deldom = 0
        for point in archive.points:
            if point != cur_point:
                pd = Point.pareto_dominance(new_point, point)
                if pd < 0:
                    deldom = deldom + archive.calculate_dom(new_point, point)
                    k1 = k1 + 1
                elif pd == 0:
                    k2 = k2 + 1
                elif pd > 0:
                    k3 = k3 + 1
                    dominated_points.append(point)
        # Case 2a If new point is dominated by k(k>=1) points in the archive
        if k1 > 0:
            deldom_avg = deldom / k1
            e = float()
            try:
                e = math.exp(deldom_avg / temp)
            except OverflowError:
                e = math.inf
            prob = 1.0 / (1.0 + e)
            if random.random() <= prob:
                cur_point = new_point
        # Case 3b If new point is non-dominated wrt to all points in the archive
        elif k2 == archive.points.size:
            archive.add(new_point)
            cur_point = new_point
        # Case 3c If new point dominates k(k>=1) points in the archive
        elif k3 > 0:
            archive.remove_value(dominated_points)
            archive.add(new_point)
            cur_point = new_point
            pass

    elif dominance < 0:  # Case 3 new_point dominates cur_point
        case = 3
        k1 = 0
        k2 = 0
        k3 = 0
        dominated_points = []
        deldom_min = math.inf
        point_deldom_min = None
        for point in archive.points:
            if point != cur_point:
                pd = Point.pareto_dominance(new_point, point)
                if pd < 0:
                    k1 = k1 + 1
                    deldom = archive.calculate_dom(new_point, point)
                    if deldom < deldom_min:
                        deldom_min = deldom
                        point_deldom_min = point
                elif pd == 0:
                    k2 = k2 + 1
                elif pd > 0:
                    k3 = k3 + 1
                    dominated_points.append(point)
        # Case 3a If new point is dominated by k(k>=1) points in the archive
        if k1 > 0:
            prob = 1.0 / (1.0 + math.exp(-deldom_min))
            if random.random() <= prob:
                cur_point = point_deldom_min
            else:
                cur_point = new_point
        # Case 3b If new point is non-dominated wrt to all points in the archive
        elif k2 == archive.points.size:
            archive.remove_value(cur_point)
            archive.add(new_point)
            cur_point = new_point
        # Case 3c If new point dominates k(k>=1) points in the archive
        elif k3 > 0:
            archive.remove_value(dominated_points)
            archive.add(new_point)
            cur_point = new_point
            pass

    return cur_point
