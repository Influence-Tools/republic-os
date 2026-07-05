---
type: Jurisdiction
title: "Autauga County, AL"
classification: county
fips: "01001"
state: "AL"
demographics:
  population: 59947
  population_under_18: 14030
  population_18_64: 36158
  population_65_plus: 9759
  median_household_income: 72481
  poverty_rate: 11.29
  homeownership_rate: 77.06
  unemployment_rate: 2.4
  median_home_value: 207200
  gini_index: 0.4752
  vacancy_rate: 8.47
  race_white: 42822
  race_black: 12244
  race_asian: 680
  race_native: 36
  hispanic: 2289
  bachelors_plus: 17744
districts:
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 0.9942
  - to: "us/states/al/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/69"
    rel: in-district
    area_weight: 0.6622
  - to: "us/states/al/districts/house/42"
    rel: in-district
    area_weight: 0.2905
  - to: "us/states/al/districts/house/88"
    rel: in-district
    area_weight: 0.0472
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Autauga County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59947 |
| Under 18 | 14030 |
| 18–64 | 36158 |
| 65+ | 9759 |
| Median household income | 72481 |
| Poverty rate | 11.29 |
| Homeownership rate | 77.06 |
| Unemployment rate | 2.4 |
| Median home value | 207200 |
| Gini index | 0.4752 |
| Vacancy rate | 8.47 |
| White | 42822 |
| Black | 12244 |
| Asian | 680 |
| Native | 36 |
| Hispanic/Latino | 2289 |
| Bachelor's or higher | 17744 |

## Districts

- [AL-06](/us/states/al/districts/06.md) — 99% (congressional)
- [AL Senate District 30](/us/states/al/districts/senate/30.md) — 100% (state senate)
- [AL House District 69](/us/states/al/districts/house/69.md) — 66% (state house)
- [AL House District 42](/us/states/al/districts/house/42.md) — 29% (state house)
- [AL House District 88](/us/states/al/districts/house/88.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
