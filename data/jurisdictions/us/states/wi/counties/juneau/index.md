---
type: Jurisdiction
title: "Juneau County, WI"
classification: county
fips: "55057"
state: "WI"
demographics:
  population: 26689
  population_under_18: 5151
  population_18_64: 15716
  population_65_plus: 5822
  median_household_income: 67270
  poverty_rate: 13.01
  homeownership_rate: 78.13
  unemployment_rate: 3.78
  median_home_value: 177700
  gini_index: 0.4044
  vacancy_rate: 25.81
  race_white: 23481
  race_black: 605
  race_asian: 158
  race_native: 196
  hispanic: 788
  bachelors_plus: 4380
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.5408
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.4591
  - to: "us/states/wi/districts/senate/24"
    rel: in-district
    area_weight: 0.7883
  - to: "us/states/wi/districts/senate/14"
    rel: in-district
    area_weight: 0.2117
  - to: "us/states/wi/districts/house/72"
    rel: in-district
    area_weight: 0.5362
  - to: "us/states/wi/districts/house/70"
    rel: in-district
    area_weight: 0.2521
  - to: "us/states/wi/districts/house/41"
    rel: in-district
    area_weight: 0.2117
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Juneau County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26689 |
| Under 18 | 5151 |
| 18–64 | 15716 |
| 65+ | 5822 |
| Median household income | 67270 |
| Poverty rate | 13.01 |
| Homeownership rate | 78.13 |
| Unemployment rate | 3.78 |
| Median home value | 177700 |
| Gini index | 0.4044 |
| Vacancy rate | 25.81 |
| White | 23481 |
| Black | 605 |
| Asian | 158 |
| Native | 196 |
| Hispanic/Latino | 788 |
| Bachelor's or higher | 4380 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 54% (congressional)
- [WI-07](/us/states/wi/districts/07.md) — 46% (congressional)
- [WI Senate District 24](/us/states/wi/districts/senate/24.md) — 79% (state senate)
- [WI Senate District 14](/us/states/wi/districts/senate/14.md) — 21% (state senate)
- [WI House District 72](/us/states/wi/districts/house/72.md) — 54% (state house)
- [WI House District 70](/us/states/wi/districts/house/70.md) — 25% (state house)
- [WI House District 41](/us/states/wi/districts/house/41.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
