#define _GNU_SOURCE

#include <math.h>
#include <stdio.h>

#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/random.h>

static
void new_seed() {
    unsigned seed;
    if (getrandom(&seed, sizeof(seed), GRND_RANDOM) < 0) {
        srandom(seed);
    } else {
        srandom(time(NULL));
    }
}

static inline
/* random double between -1 and 1 */
double random_double(void) {
    static bool first_run = true;

    if (first_run) {
        new_seed();
        first_run = false;
    }

    long rand_int = random();

    double rand_double = ((double) rand_int) / ((double) RAND_MAX);
    return 2. * rand_double - 1.;
}


double calc_pi(int points) {
    int inside = 0;

    for (int i = 0; i < points; i++) {
        double x = random_double();
        double y = random_double();

        double dist = sqrt(x*x + y*y);

        if (dist <= 1.) {
            inside++;
        }
    }

    double area_factor = ((double) inside) / ((double) points);
    double square_area = 2. * 2.;

    double circle_area = area_factor * square_area;
    double radius = 1.;

    double pi = circle_area / (radius * radius);

    return pi;
}

int main(int argc, char const *argv[]) {
    for (int i = 1; i < argc; i++) {
        int points = atoi(argv[i]);

        if (points > 0) {
            double pi = calc_pi(points);

            printf("With %d points, Monte Carlo's give us: pi = %lf.\n",
                points, pi
            );
        }
    }

    return 0;
}
