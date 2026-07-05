---
type: Jurisdiction
title: "Rockingham County, VA"
classification: county
fips: "51165"
state: "VA"
demographics:
  population: 85600
  population_under_18: 18926
  population_18_64: 49489
  population_65_plus: 17185
  median_household_income: 80693
  poverty_rate: 9.78
  homeownership_rate: 75.27
  unemployment_rate: 2.73
  median_home_value: 313000
  gini_index: 0.4495
  vacancy_rate: 10.57
  race_white: 73563
  race_black: 2060
  race_asian: 943
  race_native: 327
  hispanic: 7966
  bachelors_plus: 23937
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/va/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/34"
    rel: in-district
    area_weight: 0.3641
  - to: "us/states/va/districts/house/35"
    rel: in-district
    area_weight: 0.3374
  - to: "us/states/va/districts/house/33"
    rel: in-district
    area_weight: 0.2983
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Rockingham County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 85600 |
| Under 18 | 18926 |
| 18–64 | 49489 |
| 65+ | 17185 |
| Median household income | 80693 |
| Poverty rate | 9.78 |
| Homeownership rate | 75.27 |
| Unemployment rate | 2.73 |
| Median home value | 313000 |
| Gini index | 0.4495 |
| Vacancy rate | 10.57 |
| White | 73563 |
| Black | 2060 |
| Asian | 943 |
| Native | 327 |
| Hispanic/Latino | 7966 |
| Bachelor's or higher | 23937 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 2](/us/states/va/districts/senate/2.md) — 100% (state senate)
- [VA House District 34](/us/states/va/districts/house/34.md) — 36% (state house)
- [VA House District 35](/us/states/va/districts/house/35.md) — 34% (state house)
- [VA House District 33](/us/states/va/districts/house/33.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
