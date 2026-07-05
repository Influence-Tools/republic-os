---
type: Jurisdiction
title: "Talladega County, AL"
classification: county
fips: "01121"
state: "AL"
demographics:
  population: 81021
  population_under_18: 18278
  population_18_64: 25276
  population_65_plus: 37467
  median_household_income: 57776
  poverty_rate: 17.81
  homeownership_rate: 71.96
  unemployment_rate: 6.83
  median_home_value: 149200
  gini_index: 0.4581
  vacancy_rate: 12.72
  race_white: 50485
  race_black: 24143
  race_asian: 480
  race_native: 118
  hispanic: 1947
  bachelors_plus: 14132
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9468
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 0.0532
  - to: "us/states/al/districts/senate/11"
    rel: in-district
    area_weight: 0.503
  - to: "us/states/al/districts/senate/12"
    rel: in-district
    area_weight: 0.4968
  - to: "us/states/al/districts/house/33"
    rel: in-district
    area_weight: 0.4755
  - to: "us/states/al/districts/house/32"
    rel: in-district
    area_weight: 0.2571
  - to: "us/states/al/districts/house/35"
    rel: in-district
    area_weight: 0.2253
  - to: "us/states/al/districts/house/36"
    rel: in-district
    area_weight: 0.042
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Talladega County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 81021 |
| Under 18 | 18278 |
| 18–64 | 25276 |
| 65+ | 37467 |
| Median household income | 57776 |
| Poverty rate | 17.81 |
| Homeownership rate | 71.96 |
| Unemployment rate | 6.83 |
| Median home value | 149200 |
| Gini index | 0.4581 |
| Vacancy rate | 12.72 |
| White | 50485 |
| Black | 24143 |
| Asian | 480 |
| Native | 118 |
| Hispanic/Latino | 1947 |
| Bachelor's or higher | 14132 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 95% (congressional)
- [AL-06](/us/states/al/districts/06.md) — 5% (congressional)
- [AL Senate District 11](/us/states/al/districts/senate/11.md) — 50% (state senate)
- [AL Senate District 12](/us/states/al/districts/senate/12.md) — 50% (state senate)
- [AL House District 33](/us/states/al/districts/house/33.md) — 48% (state house)
- [AL House District 32](/us/states/al/districts/house/32.md) — 26% (state house)
- [AL House District 35](/us/states/al/districts/house/35.md) — 23% (state house)
- [AL House District 36](/us/states/al/districts/house/36.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
