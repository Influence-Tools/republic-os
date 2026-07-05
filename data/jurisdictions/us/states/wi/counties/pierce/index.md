---
type: Jurisdiction
title: "Pierce County, WI"
classification: county
fips: "55093"
state: "WI"
demographics:
  population: 42584
  population_under_18: 8644
  population_18_64: 26803
  population_65_plus: 7137
  median_household_income: 92109
  poverty_rate: 9.77
  homeownership_rate: 75.03
  unemployment_rate: 3.25
  median_home_value: 333700
  gini_index: 0.4465
  vacancy_rate: 7.49
  race_white: 39265
  race_black: 242
  race_asian: 501
  race_native: 60
  hispanic: 1280
  bachelors_plus: 12201
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wi/districts/senate/10"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wi/districts/house/29"
    rel: in-district
    area_weight: 0.6797
  - to: "us/states/wi/districts/house/28"
    rel: in-district
    area_weight: 0.179
  - to: "us/states/wi/districts/house/30"
    rel: in-district
    area_weight: 0.1407
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Pierce County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42584 |
| Under 18 | 8644 |
| 18–64 | 26803 |
| 65+ | 7137 |
| Median household income | 92109 |
| Poverty rate | 9.77 |
| Homeownership rate | 75.03 |
| Unemployment rate | 3.25 |
| Median home value | 333700 |
| Gini index | 0.4465 |
| Vacancy rate | 7.49 |
| White | 39265 |
| Black | 242 |
| Asian | 501 |
| Native | 60 |
| Hispanic/Latino | 1280 |
| Bachelor's or higher | 12201 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 10](/us/states/wi/districts/senate/10.md) — 100% (state senate)
- [WI House District 29](/us/states/wi/districts/house/29.md) — 68% (state house)
- [WI House District 28](/us/states/wi/districts/house/28.md) — 18% (state house)
- [WI House District 30](/us/states/wi/districts/house/30.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
