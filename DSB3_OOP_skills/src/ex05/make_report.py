from analytics import Research
from config import *


def main():
    try:
        research = Research(file_name)
        data = research.file_reader()
        analyser = research.Analytics(data)
        heads, tails = analyser.counts()
        p_h, p_t = analyser.fractions()
        forecast = analyser.predict_random(num_of_steps)
        h_forecasted = sum(map(lambda x: x[0], forecast))
        t_forecasted = sum(map(lambda x: x[1], forecast))
        data_to_save = generate_report(len(data), tails, heads, p_t, p_h, t_forecasted, h_forecasted)
        analyser.save_file(data_to_save, output_file_name, output_extension)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()