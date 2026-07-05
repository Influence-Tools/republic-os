---
type: Jurisdiction
title: "Amherst County, VA"
classification: county
fips: "51009"
state: "VA"
demographics:
  population: 31485
  population_under_18: 6296
  population_18_64: 18330
  population_65_plus: 6859
  median_household_income: 68724
  poverty_rate: 10.77
  homeownership_rate: 80.84
  unemployment_rate: 4.65
  median_home_value: 212400
  gini_index: 0.4399
  vacancy_rate: 11.63
  race_white: 23348
  race_black: 5358
  race_asian: 217
  race_native: 67
  hispanic: 926
  bachelors_plus: 7606
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/va/districts/senate/11"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/53"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Amherst County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31485 |
| Under 18 | 6296 |
| 18–64 | 18330 |
| 65+ | 6859 |
| Median household income | 68724 |
| Poverty rate | 10.77 |
| Homeownership rate | 80.84 |
| Unemployment rate | 4.65 |
| Median home value | 212400 |
| Gini index | 0.4399 |
| Vacancy rate | 11.63 |
| White | 23348 |
| Black | 5358 |
| Asian | 217 |
| Native | 67 |
| Hispanic/Latino | 926 |
| Bachelor's or higher | 7606 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 11](/us/states/va/districts/senate/11.md) — 100% (state senate)
- [VA House District 53](/us/states/va/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
