import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"
    domain_file.write("Propositions:\n")

    for i in range(m_):
        domain_file.write(pegs[i])
        domain_file.write(' ')

    # We refer to bottom of each peg as d_n because it is bigger than any
    # other disk and we can put any other disk above it.
    for i in range(n_ + 1):
        domain_file.write("d_" + str(i))
        domain_file.write(' ')

    for i in range(n_ + 1):
        for j in pegs:
            domain_file.write("d_" + str(i) + "_topOf_" + j)
            domain_file.write(' ')

    # for i in range(n_ + 1):
    #     for j in range(i):
    #         domain_file.write("d_%s_smaller_d_%s" % j % i)

    for i in range(n_ + 1):
        for j in range(i):
            domain_file.write("d_%s_above_d_%s" % (j, i))
            domain_file.write(' ')

    domain_file.write("\n")

    domain_file.write("Actions:\n")

    for disk in range(n_):
        for disk1 in range(disk + 1, n_ + 1):
            for peg1 in range(m_):
                for peg2 in range(m_):
                    # pegs cannot be identical
                    if peg1 == peg2:
                        continue
                    for disk2 in range(disk + 1, n_ + 1):
                        # two physical disks cannot be the same
                        if disk1 == disk2 and disk1 != n_:
                            continue
                        domain_file.write("Name: Move_d%s_d%s_p%s_p%s_d%s\n" % (disk, disk1, peg1, peg2, disk2))
                        domain_file.write(
                            # "pre: d_%s_topOf_p_%s d_%s_topOf_p_%s d_%s_above_d_%s d_%s_smaller_d_%s\n"
                            "pre: d_%s_topOf_p_%s d_%s_topOf_p_%s d_%s_above_d_%s\n"
                            # % disk % peg1 % disk2 % peg2 % disk % disk1 % disk % disk2
                            % (disk, peg1, disk2, peg2, disk, disk1)
                                          )
                        domain_file.write(
                            "add: d_%s_topOf_p_%s d_%s_topOf_p_%s d_%s_above_d_%s\n"
                            % (disk, peg2, disk1, peg1, disk, disk2)
                        )
                        domain_file.write(
                            "delete: d_%s_topOf_p_%s d_%s_above_d_%s d_%s_topOf_p_%s\n"
                            % (disk, peg1, disk, disk1, disk2, peg2)
                        )

    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"
    problem_file.write("Initial state: ")

    problem_file.write(disks[0] + "_topOf_" + pegs[0])
    problem_file.write(' ')

    for disk in range(n_):
        problem_file.write("d_" + str(disk) + "_above_" + "d_" + str(disk + 1))
        problem_file.write(' ')

    for peg in range(1, m_):
        problem_file.write("d_" + str(n_) + "_topOf_" + pegs[peg])
        problem_file.write(' ')

    problem_file.write('\n')

    problem_file.write("Goal state: ")

    problem_file.write(disks[0] + "_topOf_" + pegs[m_ - 1])
    problem_file.write(' ')

    for disk in range(n_):
        problem_file.write("d_" + str(disk) + "_above_" + "d_" + str(disk + 1))
        problem_file.write(' ')

    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
