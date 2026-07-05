---
type: Jurisdiction
title: "Alleghany County, VA"
classification: county
fips: "51005"
state: "VA"
demographics:
  population: 14859
  population_under_18: 2743
  population_18_64: 8211
  population_65_plus: 3905
  median_household_income: 56188
  poverty_rate: 11.64
  homeownership_rate: 82.28
  unemployment_rate: 2.28
  median_home_value: 125800
  gini_index: 0.4706
  vacancy_rate: 19.34
  race_white: 13664
  race_black: 778
  race_asian: 60
  race_native: 16
  hispanic: 237
  bachelors_plus: 2314
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/37"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Alleghany County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14859 |
| Under 18 | 2743 |
| 18–64 | 8211 |
| 65+ | 3905 |
| Median household income | 56188 |
| Poverty rate | 11.64 |
| Homeownership rate | 82.28 |
| Unemployment rate | 2.28 |
| Median home value | 125800 |
| Gini index | 0.4706 |
| Vacancy rate | 19.34 |
| White | 13664 |
| Black | 778 |
| Asian | 60 |
| Native | 16 |
| Hispanic/Latino | 237 |
| Bachelor's or higher | 2314 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
