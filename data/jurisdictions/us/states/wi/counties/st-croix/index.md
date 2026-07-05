---
type: Jurisdiction
title: "St. Croix County, WI"
classification: county
fips: "55109"
state: "WI"
demographics:
  population: 96033
  population_under_18: 22839
  population_18_64: 57832
  population_65_plus: 15362
  median_household_income: 103046
  poverty_rate: 6.6
  homeownership_rate: 78.32
  unemployment_rate: 2.57
  median_home_value: 377700
  gini_index: 0.4091
  vacancy_rate: 3.7
  race_white: 88464
  race_black: 662
  race_asian: 1067
  race_native: 60
  hispanic: 2935
  bachelors_plus: 34263
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wi/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/house/28"
    rel: in-district
    area_weight: 0.801
  - to: "us/states/wi/districts/house/30"
    rel: in-district
    area_weight: 0.1988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# St. Croix County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 96033 |
| Under 18 | 22839 |
| 18–64 | 57832 |
| 65+ | 15362 |
| Median household income | 103046 |
| Poverty rate | 6.6 |
| Homeownership rate | 78.32 |
| Unemployment rate | 2.57 |
| Median home value | 377700 |
| Gini index | 0.4091 |
| Vacancy rate | 3.7 |
| White | 88464 |
| Black | 662 |
| Asian | 1067 |
| Native | 60 |
| Hispanic/Latino | 2935 |
| Bachelor's or higher | 34263 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 10](/us/states/wi/districts/senate/10.md) — 100% (state senate)
- [WI House District 28](/us/states/wi/districts/house/28.md) — 80% (state house)
- [WI House District 30](/us/states/wi/districts/house/30.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
