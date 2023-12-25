from textwrap import wrap

import altair as alt
import numpy as np
import pandas as pd


# Using color as the encoding channel
def part_one_variant_one(evolution_of_life_expectancy_data, xticks,
                         separation_grid_lines):
    color_scheme = {"Africa": "cyan",
                    "Americas": "green",
                    "Asia": "red",
                    "Europe": "orange",
                    "Oceania": "blue"}
    variant_one = ((alt.Chart(evolution_of_life_expectancy_data,
                              title=alt.TitleParams(
                                  text=wrap("Evolution of life expectancy over years (encoding with color)", 39),
                                  fontSize=40))
                    .mark_circle()
                    .encode(x=alt.X("year_with_offset:Q",
                                    axis=alt.Axis(grid=False, title="Year", values=xticks, format='d'),
                                    scale=alt.Scale(domain=[evolution_of_life_expectancy_data["year"].min(),
                                                            evolution_of_life_expectancy_data["year"].max()])),
                            y=alt.Y("lifeExp:Q", axis=alt.Axis(grid=False, title="Life expectancy"),
                                    scale=alt.Scale(domain=[evolution_of_life_expectancy_data["lifeExp"].min() - 1,
                                                            evolution_of_life_expectancy_data["lifeExp"].max() + 1])),
                            color=alt.Color("continent:N", scale=alt.Scale(domain=list(color_scheme.keys()),
                                                                           range=list(color_scheme.values())),
                                            legend=alt.Legend(title=wrap("Continent's Colors", 11))),
                            size=alt.value(100))).properties(width=1800, height=900))

    variant_one = alt.layer(separation_grid_lines, variant_one)

    return variant_one


# Using shape as the encoding channel
def part_one_variant_two(evolution_of_life_expectancy_data, xticks, separation_grid_lines):
    continent_shapes = {
        'Asia': 'circle',
        'Europe': 'cross',
        'Africa': 'square',
        'Americas': 'diamond',
        'Oceania': 'triangle'
    }

    variation_two = (alt.Chart(evolution_of_life_expectancy_data,
                               title=alt.TitleParams(
                                   text=wrap("Evolution of life expectancy over years (encoding with shape)", 39),
                                   fontSize=40))
                     .mark_point(color="#000000", opacity=0.6)
                     .encode(x=alt.X("year_with_offset:Q",
                                     axis=alt.Axis(grid=False, title="Year",
                                                   values=xticks, format='d'),
                                     scale=alt.Scale(
                                         domain=[evolution_of_life_expectancy_data["year"].min(),
                                                 evolution_of_life_expectancy_data["year"].max()])),
                             y=alt.Y("lifeExp:Q", axis=alt.Axis(grid=False,
                                                                title="Life expectancy"),
                                     scale=alt.Scale(
                                         domain=[evolution_of_life_expectancy_data["lifeExp"].min() - 1,
                                                 evolution_of_life_expectancy_data["lifeExp"].max() + 1])),
                             shape=alt.Shape("continent:N", legend=alt.Legend(
                                 title=wrap("Continent's Shapes", 11)),
                                             scale=alt.Scale(range=list(continent_shapes.values()))),
                             size=alt.value(100)).properties(width=1800, height=900))

    variation_two = alt.layer(separation_grid_lines, variation_two)

    return variation_two


# Using brightness as the encoding channel
def part_one_variant_three(evolution_of_life_expectancy_data, xticks, separation_grid_lines):
    brightness_scheme = {
        "Europe": "#e3dede",
        "Oceania": "#b3afaf",
        "Americas": "#7a7777",
        "Asia": "#3b3939",
        "Africa": "#000000"
    }

    variant_three = ((alt.Chart(evolution_of_life_expectancy_data,
                                title=alt.TitleParams(
                                    text=wrap("Evolution of life expectancy over years (encoding with brightness)", 39),
                                    fontSize=40))
                      .mark_circle()
                      .encode(x=alt.X("year_with_offset:Q",
                                      axis=alt.Axis(grid=False, title="Year",
                                                    values=xticks, format='d'),
                                      scale=alt.Scale(
                                          domain=[evolution_of_life_expectancy_data["year"].min(),
                                                  evolution_of_life_expectancy_data["year"].max()])),
                              y=alt.Y("lifeExp:Q", axis=alt.Axis(grid=False, title="Life expectancy"),
                                      scale=alt.Scale(domain=[evolution_of_life_expectancy_data["lifeExp"].min() - 1,
                                                              evolution_of_life_expectancy_data[
                                                                  "lifeExp"].max() + 1])),
                              color=alt.Color("continent:N", scale=alt.Scale(domain=list(brightness_scheme.keys()),
                                                                             range=list(brightness_scheme.values())),
                                              legend=alt.Legend(title=wrap("Continent's Brightness", 11))),
                              size=alt.value(100))).properties(width=1800, height=900))

    variant_three = alt.layer(separation_grid_lines, variant_three)

    return variant_three


def part_one(evolution_of_life_expectancy_data, x_tickers, separation_grid_lines):
    variant_one = (part_one_variant_one(evolution_of_life_expectancy_data, x_tickers, separation_grid_lines)
                   .configure_title(offset=20).configure_axis(labelFontSize=25, titleFontSize=30)
                   .configure_legend(labelFontSize=25, titleFontSize=30))

    variant_two = (part_one_variant_two(evolution_of_life_expectancy_data, x_tickers, separation_grid_lines)
                   .configure_title(offset=20).configure_axis(labelFontSize=25, titleFontSize=30)
                   .configure_legend(labelFontSize=25, titleFontSize=30))

    variant_three = (part_one_variant_three(evolution_of_life_expectancy_data, x_tickers, separation_grid_lines)
                     .configure_title(offset=20).configure_axis(labelFontSize=25, titleFontSize=30)
                     .configure_legend(labelFontSize=25, titleFontSize=30))

    return variant_one, variant_two, variant_three


# Using size as the encoding channel
def part_two_variant_one(correlation_between_wealth_and_health):
    variant_one = ((alt.Chart(correlation_between_wealth_and_health,
                              title=alt.TitleParams(
                                  text=wrap("Correlation between wealth and health (encoding with size)", 39),
                                  fontSize=40))
                    .mark_circle()
                    .encode(x=alt.X("gdpPercap:Q",
                                    axis=alt.Axis(grid=True, title="GDP per capita"),
                                    scale=alt.Scale(domain=[
                                        correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                                        correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
                            y=alt.Y("lifeExp:Q", axis=alt.Axis(grid=True, title="Life expectancy"),
                                    scale=alt.Scale(domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                                            correlation_between_wealth_and_health[
                                                                "lifeExp"].max() + 1])),
                            size=alt.Size("pop:Q", scale=alt.Scale(
                                domain=[correlation_between_wealth_and_health["pop"].min(),
                                        correlation_between_wealth_and_health["pop"].max()], range=[40, 1000]),
                                          legend=alt.Legend(title=wrap("Population's Size", 12)))))
                   .properties(width=1800, height=900))

    return variant_one


# Using brightness as the encoding channel
def part_two_variant_two(correlation_between_wealth_and_health):
    brightness_scheme = {
        200000000: "#e3dede",
        450000000: "#b3afaf",
        700000000: "#7a7777",
        950000000: "#3b3939",
        1200000000: "#000000"
    }
    variant_two = alt.layer(
        alt.Chart(correlation_between_wealth_and_health[
                      correlation_between_wealth_and_health['pop'] < 200000000], title=alt.TitleParams(
            text=wrap("Correlation between wealth and health (encoding with brightness)", 39),
            fontSize=40)).mark_circle(stroke="black",
                                      strokeWidth=1).encode(
            x=alt.X("gdpPercap:Q", axis=alt.Axis(title="GDP per capita"), scale=alt.Scale(domain=[
                correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
            y=alt.Y("lifeExp:Q", axis=alt.Axis(title="Life expectancy"),
                    scale=alt.Scale(domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                            correlation_between_wealth_and_health["lifeExp"].max() + 1])),
            color=alt.Color("pop:Q", scale=alt.Scale(domain=list(brightness_scheme.keys()),
                                                     range=list(brightness_scheme.values())),
                            legend=alt.Legend(title=wrap("Population's Brightness", 12))),
            size=alt.value(100)
        ),
        alt.Chart(correlation_between_wealth_and_health[(correlation_between_wealth_and_health['pop'] >= 200000000) & (
                correlation_between_wealth_and_health['pop'] < 400000000)]).mark_circle(stroke="black",
                                                                                        strokeWidth=1).encode(
            x=alt.X("gdpPercap:Q", axis=alt.Axis(title="GDP per capita"), scale=alt.Scale(domain=[
                correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
            y=alt.Y("lifeExp:Q", axis=alt.Axis(title="Life expectancy"),
                    scale=alt.Scale(domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                            correlation_between_wealth_and_health["lifeExp"].max() + 1])),
            color=alt.Color("pop:Q", scale=alt.Scale(domain=list(brightness_scheme.keys()),
                                                     range=list(brightness_scheme.values())),
                            legend=alt.Legend(title=wrap("Population's Brightness", 12))),
            size=alt.value(100)
        ),
        alt.Chart(correlation_between_wealth_and_health[(correlation_between_wealth_and_health['pop'] >= 400000000) & (
                correlation_between_wealth_and_health['pop'] < 600000000)]).mark_circle(stroke="black",
                                                                                        strokeWidth=1).encode(
            x=alt.X("gdpPercap:Q", axis=alt.Axis(title="GDP per capita"), scale=alt.Scale(domain=[
                correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
            y=alt.Y("lifeExp:Q", axis=alt.Axis(title="Life expectancy"),
                    scale=alt.Scale(domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                            correlation_between_wealth_and_health["lifeExp"].max() + 1])),
            color=alt.Color("pop:Q", scale=alt.Scale(domain=list(brightness_scheme.keys()),
                                                     range=list(brightness_scheme.values())),
                            legend=alt.Legend(title=wrap("Population's Brightness", 12))),
            size=alt.value(100)
        ),
        alt.Chart(correlation_between_wealth_and_health[(correlation_between_wealth_and_health['pop'] >= 600000000) & (
                correlation_between_wealth_and_health['pop'] < 800000000)]).mark_circle(stroke="black",
                                                                                        strokeWidth=1).encode(
            x=alt.X("gdpPercap:Q", axis=alt.Axis(title="GDP per capita"), scale=alt.Scale(domain=[
                correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
            y=alt.Y("lifeExp:Q", axis=alt.Axis(title="Life expectancy"),
                    scale=alt.Scale(domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                            correlation_between_wealth_and_health["lifeExp"].max() + 1])),
            color=alt.Color("pop:Q", scale=alt.Scale(domain=list(brightness_scheme.keys()),
                                                     range=list(brightness_scheme.values())),
                            legend=alt.Legend(title=wrap("Population's Brightness", 12))),
            size=alt.value(100)
        ),
        alt.Chart(correlation_between_wealth_and_health[
                      correlation_between_wealth_and_health['pop'] >= 800000000]).mark_circle(stroke="black",
                                                                                              strokeWidth=1).encode(
            x=alt.X("gdpPercap:Q", axis=alt.Axis(title="GDP per capita"), scale=alt.Scale(domain=[
                correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
            y=alt.Y("lifeExp:Q", axis=alt.Axis(title="Life expectancy"),
                    scale=alt.Scale(domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                            correlation_between_wealth_and_health["lifeExp"].max() + 1])),
            color=alt.Color("pop:Q", scale=alt.Scale(domain=list(brightness_scheme.keys()),
                                                     range=list(brightness_scheme.values())),
                            legend=alt.Legend(title=wrap("Population's Brightness", 12))),
            size=alt.value(100)
        )
    ).properties(width=1800, height=900)

    return variant_two


# Using orientation as the encoding channel
def part_two_variant_three(correlation_between_wealth_and_health):
    correlation_between_wealth_and_health['angle'] = -45 * (correlation_between_wealth_and_health['pop'] -
                                                            correlation_between_wealth_and_health['pop'].min()) / (
                                                             correlation_between_wealth_and_health['pop'].max() -
                                                             correlation_between_wealth_and_health['pop'].min())

    correlation_between_wealth_and_health['size'] = 1

    variant_three = ((alt.Chart(correlation_between_wealth_and_health,
                                title=alt.TitleParams(
                                    text=wrap("Correlation between wealth and health (encoding with orientation)", 39),
                                    fontSize=40))
                      .mark_point(shape='stroke', color="#000000", strokeWidth=2)
                      .encode(x=alt.X("gdpPercap:Q",
                                      axis=alt.Axis(grid=True, title="GDP per capita"),
                                      scale=alt.Scale(domain=[
                                          correlation_between_wealth_and_health["gdpPercap"].min() - 2000,
                                          correlation_between_wealth_and_health["gdpPercap"].max() + 2000])),
                              y=alt.Y("lifeExp:Q", axis=alt.Axis(grid=True, title="Life expectancy"),
                                      scale=alt.Scale(
                                          domain=[correlation_between_wealth_and_health["lifeExp"].min() - 1,
                                                  correlation_between_wealth_and_health[
                                                      "lifeExp"].max() + 1])),
                              size=alt.Size("size", legend=None),
                              angle=alt.Angle("pop:Q"),
                              tooltip=[alt.Tooltip("pop:Q", title="Population")],
                              ))
                     .properties(width=1800, height=900))

    legend_content = pd.DataFrame({
        "label_one": [
            "⎯  200,000,000"

        ],
        "label_two": [
            "\   400,000,000"
        ],
        "label_three": [
            "|   800,000,000"
        ],
        "label_four": [
            "/   1,200,000,000"

        ]
    })

    # Create the legend
    legend_title_text = alt.Chart(pd.DataFrame({"title": [wrap("Population's Orientation", 12)]})).mark_text(
        dx=1010, dy=-437, fontSize=30, fontStyle="bold").encode(text="title")

    legend_label_one = (
        alt.Chart(legend_content).mark_text(dx=985, dy=-370, fontSize=20,
                                            stroke="black", strokeWidth=0.4)
        .encode(y=alt.Y("label_one", axis=None), text="label_one"))

    legend_label_two = (
        alt.Chart(legend_content).mark_text(dx=990, dy=-340, fontSize=20,
                                            stroke="black", strokeWidth=0.4)
        .encode(y=alt.Y("label_two", axis=None), text="label_two"))

    legend_label_three = (
        alt.Chart(legend_content).mark_text(dx=990, dy=-610, fontSize=20,
                                            stroke="black", strokeWidth=0.4)
        .encode(y=alt.Y("label_three", axis=None), text="label_three"))

    legend_label_four = (
        alt.Chart(legend_content).mark_text(dx=998, dy=20, fontSize=20,
                                            stroke="black", strokeWidth=0.4)
        .encode(y=alt.Y("label_four", axis=None), text="label_four"))

    # Combine all elements to make the legend
    legend = legend_title_text + legend_label_two + legend_label_three + legend_label_four

    # Combine the main chart and the legend chart
    final_chart = alt.layer(variant_three, legend, legend_label_one)
    return final_chart


def part_two(gapminder_data):
    variant_one = (part_two_variant_one(gapminder_data)
                   .configure_title(offset=20).configure_axis(labelFontSize=20, titleFontSize=25)
                   .configure_legend(labelFontSize=25, titleFontSize=30))
    variant_two = (part_two_variant_two(gapminder_data)
                   .configure_title(offset=20).configure_axis(labelFontSize=20, titleFontSize=25)
                   .configure_legend(labelFontSize=20, titleFontSize=30))
    variant_three = (part_two_variant_three(gapminder_data)
                     .configure_title(offset=20).configure_axis(labelFontSize=20, titleFontSize=25)
                     .configure_legend(labelFontSize=20, titleFontSize=30))
    return variant_one, variant_two, variant_three


def part_three(evolution_of_life_expectancy_data, x_tickers, separation_grid_lines):
    custom_color_scale = {
        20: '#CCCCCC',
        35: '#999999',
        50: '#666666',
        65: '#333333',
        80: '#000000'
    }

    variant_one = ((alt.Chart(evolution_of_life_expectancy_data,
                              title=alt.TitleParams(
                                  text=wrap(
                                      "GDP per capita over time (encoded with life expectancy, population "
                                      "and continent)",
                                      39),
                                  fontSize=40))
                    .mark_point(color="#000000")
                    .encode(x=alt.X("year_with_offset:Q",
                                    axis=alt.Axis(grid=False, title="Year", values=x_tickers, format='d'),
                                    scale=alt.Scale(domain=[evolution_of_life_expectancy_data["year"].min(),
                                                            evolution_of_life_expectancy_data["year"].max()])),
                            y=alt.Y("gdpPercap:Q", axis=alt.Axis(grid=False, title="GDP per capita"),
                                    scale=alt.Scale(domain=[evolution_of_life_expectancy_data["gdpPercap"].min() - 1000,
                                                            evolution_of_life_expectancy_data[
                                                                "gdpPercap"].max() + 5000])),
                            size=alt.Size("pop:Q", scale=alt.Scale(scheme='viridis',
                                                                   domain=[
                                                                       evolution_of_life_expectancy_data["pop"].min(),
                                                                       evolution_of_life_expectancy_data["pop"].max()],
                                                                   range=[200, 1000]),
                                          legend=alt.Legend(title=wrap("Population's Size", 12))),
                            shape=alt.Shape("continent:N", legend=alt.Legend(symbolSize=500,
                                                                             title=wrap("Continent's Shapes", 11))),
                            tooltip=[alt.Tooltip("lifeExp:Q", title="lifeExp")],
                            color=alt.Color(
                                "lifeExp:Q",
                                scale=alt.Scale(domain=list(custom_color_scale.keys()),
                                                range=list(custom_color_scale.values()), reverse=True),
                                legend=alt.Legend(title=wrap("Life Expect-ancy's Brightness", 11)),
                            )
                            )).properties(width=1800, height=900))

    variant_one = alt.layer(separation_grid_lines, variant_one)

    return variant_one.configure_axis(labelFontSize=20, titleFontSize=25).configure_legend(labelFontSize=20,
                                                                                           titleFontSize=30)


def main():
    # Read the csv file
    gapminder_data = pd.read_csv("gapminder.csv", header=0)
    # Use seed to replicate same "jittering" for all graphs
    np.random.seed(3)
    offsets_to_avoid_overlapping = np.random.uniform(low=-1.5, high=1.5, size=len(gapminder_data))
    gapminder_data["year_with_offset"] = gapminder_data["year"] + offsets_to_avoid_overlapping
    x_tickers = sorted(list(set(gapminder_data["year"])))
    grid_x_values = []
    for i, value in enumerate(x_tickers):
        if i == 0:
            grid_x_values.append(value + 2.5)
        elif i == len(x_tickers) - 1:
            grid_x_values.append(value - 2.5)
        else:
            grid_x_values.append(value - 2.5)
            grid_x_values.append(value + 2.5)
    vertical_line_data = pd.DataFrame({'year': grid_x_values})
    separation_grid_lines = (alt.Chart(vertical_line_data).mark_rule(color='gray', strokeDash=[2, 2])
                             .encode(x=alt.X("year",
                                             axis=alt.Axis(grid=False),
                                             scale=alt.Scale(
                                                 domain=[gapminder_data["year"].min() - 2.5,
                                                         gapminder_data["year"].max() + 2.5])))
                             .properties(width=1800, height=900))

    variant_one, variant_two, variant_three = part_one(gapminder_data, x_tickers, separation_grid_lines)
    variant_one.save(embed_options={"actions": False}, fp="part_one_variant_one.html")
    variant_two.save(embed_options={"actions": False}, fp="part_one_variant_two.html")
    variant_three.save(embed_options={"actions": False}, fp="part_one_variant_three.html")

    variant_one, variant_two, variant_three = part_two(gapminder_data)
    variant_one.save(embed_options={"actions": False}, fp="part_two_variant_one.html")
    variant_two.save(embed_options={"actions": False}, fp="part_two_variant_two.html")
    variant_three.save(embed_options={"actions": False}, fp="part_two_variant_three.html")

    part_three_chart = part_three(gapminder_data, x_tickers, separation_grid_lines)
    part_three_chart.save(embed_options={"actions": False}, fp="part_three.html")


if __name__ == '__main__':
    main()
