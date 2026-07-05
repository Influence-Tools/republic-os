---
type: Jurisdiction
title: "Newton County, IN"
classification: county
fips: "18111"
state: "IN"
demographics:
  population: 13922
  population_under_18: 2890
  population_18_64: 8213
  population_65_plus: 2819
  median_household_income: 75481
  poverty_rate: 14.04
  homeownership_rate: 81.1
  unemployment_rate: 6.52
  median_home_value: 171500
  gini_index: 0.3856
  vacancy_rate: 6.02
  race_white: 12108
  race_black: 147
  race_asian: 72
  race_native: 22
  hispanic: 1173
  bachelors_plus: 2018
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/in/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/11"
    rel: in-district
    area_weight: 0.8005
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.1995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Newton County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13922 |
| Under 18 | 2890 |
| 18–64 | 8213 |
| 65+ | 2819 |
| Median household income | 75481 |
| Poverty rate | 14.04 |
| Homeownership rate | 81.1 |
| Unemployment rate | 6.52 |
| Median home value | 171500 |
| Gini index | 0.3856 |
| Vacancy rate | 6.02 |
| White | 12108 |
| Black | 147 |
| Asian | 72 |
| Native | 22 |
| Hispanic/Latino | 1173 |
| Bachelor's or higher | 2018 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 6](/us/states/in/districts/senate/6.md) — 100% (state senate)
- [IN House District 11](/us/states/in/districts/house/11.md) — 80% (state house)
- [IN House District 13](/us/states/in/districts/house/13.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
