---
type: Jurisdiction
title: "Berrien County, MI"
classification: county
fips: "26021"
state: "MI"
demographics:
  population: 153288
  population_under_18: 32692
  population_18_64: 87893
  population_65_plus: 32703
  median_household_income: 65425
  poverty_rate: 15.08
  homeownership_rate: 72.83
  unemployment_rate: 6.17
  median_home_value: 224300
  gini_index: 0.4748
  vacancy_rate: 17.18
  race_white: 113353
  race_black: 20232
  race_asian: 2761
  race_native: 409
  hispanic: 9697
  bachelors_plus: 46853
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.2792
  - to: "us/states/mi/districts/04"
    rel: in-district
    area_weight: 0.0875
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 0.2208
  - to: "us/states/mi/districts/senate/20"
    rel: in-district
    area_weight: 0.1459
  - to: "us/states/mi/districts/house/37"
    rel: in-district
    area_weight: 0.226
  - to: "us/states/mi/districts/house/38"
    rel: in-district
    area_weight: 0.0957
  - to: "us/states/mi/districts/house/39"
    rel: in-district
    area_weight: 0.045
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Berrien County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 153288 |
| Under 18 | 32692 |
| 18–64 | 87893 |
| 65+ | 32703 |
| Median household income | 65425 |
| Poverty rate | 15.08 |
| Homeownership rate | 72.83 |
| Unemployment rate | 6.17 |
| Median home value | 224300 |
| Gini index | 0.4748 |
| Vacancy rate | 17.18 |
| White | 113353 |
| Black | 20232 |
| Asian | 2761 |
| Native | 409 |
| Hispanic/Latino | 9697 |
| Bachelor's or higher | 46853 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 28% (congressional)
- [MI-04](/us/states/mi/districts/04.md) — 9% (congressional)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 22% (state senate)
- [MI Senate District 20](/us/states/mi/districts/senate/20.md) — 15% (state senate)
- [MI House District 37](/us/states/mi/districts/house/37.md) — 23% (state house)
- [MI House District 38](/us/states/mi/districts/house/38.md) — 10% (state house)
- [MI House District 39](/us/states/mi/districts/house/39.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
