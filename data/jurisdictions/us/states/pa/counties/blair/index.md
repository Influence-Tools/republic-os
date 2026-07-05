---
type: Jurisdiction
title: "Blair County, PA"
classification: county
fips: "42013"
state: "PA"
demographics:
  population: 121277
  population_under_18: 24416
  population_18_64: 70793
  population_65_plus: 26068
  median_household_income: 62382
  poverty_rate: 12.04
  homeownership_rate: 72.35
  unemployment_rate: 4.39
  median_home_value: 161100
  gini_index: 0.446
  vacancy_rate: 9.56
  race_white: 111706
  race_black: 2423
  race_asian: 849
  race_native: 37
  hispanic: 1925
  bachelors_plus: 27802
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/80"
    rel: in-district
    area_weight: 0.8355
  - to: "us/states/pa/districts/house/79"
    rel: in-district
    area_weight: 0.1642
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Blair County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 121277 |
| Under 18 | 24416 |
| 18–64 | 70793 |
| 65+ | 26068 |
| Median household income | 62382 |
| Poverty rate | 12.04 |
| Homeownership rate | 72.35 |
| Unemployment rate | 4.39 |
| Median home value | 161100 |
| Gini index | 0.446 |
| Vacancy rate | 9.56 |
| White | 111706 |
| Black | 2423 |
| Asian | 849 |
| Native | 37 |
| Hispanic/Latino | 1925 |
| Bachelor's or higher | 27802 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 30](/us/states/pa/districts/senate/30.md) — 100% (state senate)
- [PA House District 80](/us/states/pa/districts/house/80.md) — 84% (state house)
- [PA House District 79](/us/states/pa/districts/house/79.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
