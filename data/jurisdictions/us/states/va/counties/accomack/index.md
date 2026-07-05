---
type: Jurisdiction
title: "Accomack County, VA"
classification: county
fips: "51001"
state: "VA"
demographics:
  population: 33335
  population_under_18: 6829
  population_18_64: 17936
  population_65_plus: 8570
  median_household_income: 58993
  poverty_rate: 13.92
  homeownership_rate: 71.43
  unemployment_rate: 3.4
  median_home_value: 204300
  gini_index: 0.4495
  vacancy_rate: 34.49
  race_white: 19765
  race_black: 9061
  race_asian: 240
  race_native: 81
  hispanic: 3649
  bachelors_plus: 7384
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.449
  - to: "us/states/va/districts/senate/20"
    rel: in-district
    area_weight: 0.4292
  - to: "us/states/va/districts/house/100"
    rel: in-district
    area_weight: 0.4292
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Accomack County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33335 |
| Under 18 | 6829 |
| 18–64 | 17936 |
| 65+ | 8570 |
| Median household income | 58993 |
| Poverty rate | 13.92 |
| Homeownership rate | 71.43 |
| Unemployment rate | 3.4 |
| Median home value | 204300 |
| Gini index | 0.4495 |
| Vacancy rate | 34.49 |
| White | 19765 |
| Black | 9061 |
| Asian | 240 |
| Native | 81 |
| Hispanic/Latino | 3649 |
| Bachelor's or higher | 7384 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 45% (congressional)
- [VA Senate District 20](/us/states/va/districts/senate/20.md) — 43% (state senate)
- [VA House District 100](/us/states/va/districts/house/100.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
