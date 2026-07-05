---
type: Jurisdiction
title: "Decatur County, IN"
classification: county
fips: "18031"
state: "IN"
demographics:
  population: 26422
  population_under_18: 6208
  population_18_64: 15417
  population_65_plus: 4797
  median_household_income: 69783
  poverty_rate: 10.2
  homeownership_rate: 76.09
  unemployment_rate: 2.65
  median_home_value: 199100
  gini_index: 0.435
  vacancy_rate: 8.33
  race_white: 24649
  race_black: 178
  race_asian: 22
  race_native: 77
  hispanic: 667
  bachelors_plus: 4576
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/73"
    rel: in-district
    area_weight: 0.5484
  - to: "us/states/in/districts/house/55"
    rel: in-district
    area_weight: 0.2556
  - to: "us/states/in/districts/house/67"
    rel: in-district
    area_weight: 0.1959
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Decatur County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26422 |
| Under 18 | 6208 |
| 18–64 | 15417 |
| 65+ | 4797 |
| Median household income | 69783 |
| Poverty rate | 10.2 |
| Homeownership rate | 76.09 |
| Unemployment rate | 2.65 |
| Median home value | 199100 |
| Gini index | 0.435 |
| Vacancy rate | 8.33 |
| White | 24649 |
| Black | 178 |
| Asian | 22 |
| Native | 77 |
| Hispanic/Latino | 667 |
| Bachelor's or higher | 4576 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 100% (state senate)
- [IN House District 73](/us/states/in/districts/house/73.md) — 55% (state house)
- [IN House District 55](/us/states/in/districts/house/55.md) — 26% (state house)
- [IN House District 67](/us/states/in/districts/house/67.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
