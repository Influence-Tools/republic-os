---
type: Jurisdiction
title: "Floyd County, GA"
classification: county
fips: "13115"
state: "GA"
demographics:
  population: 99693
  population_under_18: 22606
  population_18_64: 60343
  population_65_plus: 16744
  median_household_income: 65565
  poverty_rate: 16.02
  homeownership_rate: 63.58
  unemployment_rate: 4.25
  median_home_value: 217900
  gini_index: 0.4679
  vacancy_rate: 9.93
  race_white: 70982
  race_black: 13764
  race_asian: 1463
  race_native: 784
  hispanic: 12383
  bachelors_plus: 24421
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/ga/districts/senate/52"
    rel: in-district
    area_weight: 0.7575
  - to: "us/states/ga/districts/senate/53"
    rel: in-district
    area_weight: 0.2424
  - to: "us/states/ga/districts/house/12"
    rel: in-district
    area_weight: 0.658
  - to: "us/states/ga/districts/house/13"
    rel: in-district
    area_weight: 0.2641
  - to: "us/states/ga/districts/house/5"
    rel: in-district
    area_weight: 0.0778
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Floyd County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 99693 |
| Under 18 | 22606 |
| 18–64 | 60343 |
| 65+ | 16744 |
| Median household income | 65565 |
| Poverty rate | 16.02 |
| Homeownership rate | 63.58 |
| Unemployment rate | 4.25 |
| Median home value | 217900 |
| Gini index | 0.4679 |
| Vacancy rate | 9.93 |
| White | 70982 |
| Black | 13764 |
| Asian | 1463 |
| Native | 784 |
| Hispanic/Latino | 12383 |
| Bachelor's or higher | 24421 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 52](/us/states/ga/districts/senate/52.md) — 76% (state senate)
- [GA Senate District 53](/us/states/ga/districts/senate/53.md) — 24% (state senate)
- [GA House District 12](/us/states/ga/districts/house/12.md) — 66% (state house)
- [GA House District 13](/us/states/ga/districts/house/13.md) — 26% (state house)
- [GA House District 5](/us/states/ga/districts/house/5.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
