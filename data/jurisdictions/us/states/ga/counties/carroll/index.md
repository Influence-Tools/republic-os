---
type: Jurisdiction
title: "Carroll County, GA"
classification: county
fips: "13045"
state: "GA"
demographics:
  population: 124569
  population_under_18: 29613
  population_18_64: 77253
  population_65_plus: 17703
  median_household_income: 73714
  poverty_rate: 15.37
  homeownership_rate: 71.28
  unemployment_rate: 5.9
  median_home_value: 255100
  gini_index: 0.4399
  vacancy_rate: 7.81
  race_white: 85134
  race_black: 23096
  race_asian: 1060
  race_native: 1111
  hispanic: 10771
  bachelors_plus: 26278
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ga/districts/senate/6"
    rel: in-district
    area_weight: 0.5576
  - to: "us/states/ga/districts/senate/30"
    rel: in-district
    area_weight: 0.4423
  - to: "us/states/ga/districts/house/18"
    rel: in-district
    area_weight: 0.3419
  - to: "us/states/ga/districts/house/72"
    rel: in-district
    area_weight: 0.2874
  - to: "us/states/ga/districts/house/71"
    rel: in-district
    area_weight: 0.2724
  - to: "us/states/ga/districts/house/70"
    rel: in-district
    area_weight: 0.0983
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Carroll County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 124569 |
| Under 18 | 29613 |
| 18–64 | 77253 |
| 65+ | 17703 |
| Median household income | 73714 |
| Poverty rate | 15.37 |
| Homeownership rate | 71.28 |
| Unemployment rate | 5.9 |
| Median home value | 255100 |
| Gini index | 0.4399 |
| Vacancy rate | 7.81 |
| White | 85134 |
| Black | 23096 |
| Asian | 1060 |
| Native | 1111 |
| Hispanic/Latino | 10771 |
| Bachelor's or higher | 26278 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 6](/us/states/ga/districts/senate/6.md) — 56% (state senate)
- [GA Senate District 30](/us/states/ga/districts/senate/30.md) — 44% (state senate)
- [GA House District 18](/us/states/ga/districts/house/18.md) — 34% (state house)
- [GA House District 72](/us/states/ga/districts/house/72.md) — 29% (state house)
- [GA House District 71](/us/states/ga/districts/house/71.md) — 27% (state house)
- [GA House District 70](/us/states/ga/districts/house/70.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
