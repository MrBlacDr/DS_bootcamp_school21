import sys
import resource  


def read_file_into_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def main():
    if len(sys.argv) != 2:
        print("Usage: python ordinary.py <path_to_ratings.csv>")
        return
    
    file_path = sys.argv[1]
    
    # Замеряем использование ресурсов ДО
    start_res = resource.getrusage(resource.RUSAGE_SELF)
    
    # Читаем файл
    lines = read_file_into_list(file_path)
    
    # Проходим по списку (делаем pass)
    for line in lines:
        pass
    
    # Замеряем использование ресурсов ПОСЛЕ
    end_res = resource.getrusage(resource.RUSAGE_SELF)
    
    # Вычисляем использование памяти
    # ru_maxrss - максимальный размер резидента в КБ (для Linux/Mac)
    memory_used_mb = (end_res.ru_maxrss - start_res.ru_maxrss) / 1024.0  # в МБ
    memory_used_gb = memory_used_mb / 1024.0  # в ГБ
    
    # Вычисляем время CPU (user + system)
    cpu_time_user = end_res.ru_utime - start_res.ru_utime
    cpu_time_system = end_res.ru_stime - start_res.ru_stime
    total_cpu_time = cpu_time_user + cpu_time_system
    
    
    print(f"Peak memory usage: {memory_used_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time: {total_cpu_time:.2f} s")


if __name__ == "__main__":
    main()


# "/mnt/d/s21/ml-25m/ratings.csv"