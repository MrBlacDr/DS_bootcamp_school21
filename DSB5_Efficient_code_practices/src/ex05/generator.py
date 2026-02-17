import sys
import resource


def read_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


def main():
    if len(sys.argv) != 2:
        print("Usage: python generator.py <path_to_ratings.csv>")
        return
    
    file_path = sys.argv[1]
    
    # Замеряем использование ресурсов ДО
    start_res = resource.getrusage(resource.RUSAGE_SELF)
    
    # Получаем генератор
    line_generator = read_file_generator(file_path)
    
    # Проходим по генератору (делаем pass)
    for line in line_generator:
        pass
    
    # Замеряем использование ресурсов ПОСЛЕ
    end_res = resource.getrusage(resource.RUSAGE_SELF)
    
    # Вычисляем использование памяти
    memory_used_mb = (end_res.ru_maxrss - start_res.ru_maxrss) / 1024.0
    memory_used_gb = memory_used_mb / 1024.0
    
    # Вычисляем время CPU
    cpu_time_user = end_res.ru_utime - start_res.ru_utime
    cpu_time_system = end_res.ru_stime - start_res.ru_stime
    total_cpu_time = cpu_time_user + cpu_time_system
    
    print(f"Peak memory usage: {memory_used_gb:.4f} GB")
    print(f"User Mode Time + System Mode Time: {total_cpu_time:.2f} seconds")


if __name__ == "__main__":
    main()