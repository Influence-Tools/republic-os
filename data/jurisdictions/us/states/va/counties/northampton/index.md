---
type: Jurisdiction
title: "Northampton County, VA"
classification: county
fips: "51131"
state: "VA"
demographics:
  population: 12059
  population_under_18: 2210
  population_18_64: 6307
  population_65_plus: 3542
  median_household_income: 61632
  poverty_rate: 17.73
  homeownership_rate: 66.14
  unemployment_rate: 3.34
  median_home_value: 316200
  gini_index: 0.536
  vacancy_rate: 27.99
  race_white: 6840
  race_black: 3618
  race_asian: 129
  race_native: 10
  hispanic: 1124
  bachelors_plus: 4094
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.4378
  - to: "us/states/va/districts/senate/20"
    rel: in-district
    area_weight: 0.4327
  - to: "us/states/va/districts/house/100"
    rel: in-district
    area_weight: 0.4327
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Northampton County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12059 |
| Under 18 | 2210 |
| 18–64 | 6307 |
| 65+ | 3542 |
| Median household income | 61632 |
| Poverty rate | 17.73 |
| Homeownership rate | 66.14 |
| Unemployment rate | 3.34 |
| Median home value | 316200 |
| Gini index | 0.536 |
| Vacancy rate | 27.99 |
| White | 6840 |
| Black | 3618 |
| Asian | 129 |
| Native | 10 |
| Hispanic/Latino | 1124 |
| Bachelor's or higher | 4094 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 44% (congressional)
- [VA Senate District 20](/us/states/va/districts/senate/20.md) — 43% (state senate)
- [VA House District 100](/us/states/va/districts/house/100.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
