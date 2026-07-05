---
type: Jurisdiction
title: "Manassas city, VA"
classification: county
fips: "51683"
state: "VA"
demographics:
  population: 42976
  population_under_18: 12657
  population_18_64: 15312
  population_65_plus: 15007
  median_household_income: 113590
  poverty_rate: 7.74
  homeownership_rate: 71.47
  unemployment_rate: 3.8
  median_home_value: 449900
  gini_index: 0.4055
  vacancy_rate: 2.08
  race_white: 18655
  race_black: 5153
  race_asian: 2397
  race_native: 254
  hispanic: 18865
  bachelors_plus: 12569
districts:
  - to: "us/states/va/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/30"
    rel: in-district
    area_weight: 0.9963
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Manassas city, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42976 |
| Under 18 | 12657 |
| 18–64 | 15312 |
| 65+ | 15007 |
| Median household income | 113590 |
| Poverty rate | 7.74 |
| Homeownership rate | 71.47 |
| Unemployment rate | 3.8 |
| Median home value | 449900 |
| Gini index | 0.4055 |
| Vacancy rate | 2.08 |
| White | 18655 |
| Black | 5153 |
| Asian | 2397 |
| Native | 254 |
| Hispanic/Latino | 18865 |
| Bachelor's or higher | 12569 |

## Districts

- [VA-10](/us/states/va/districts/10.md) — 100% (congressional)
- [VA Senate District 30](/us/states/va/districts/senate/30.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
