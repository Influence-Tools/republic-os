---
type: Jurisdiction
title: "Northumberland County, VA"
classification: county
fips: "51133"
state: "VA"
demographics:
  population: 12188
  population_under_18: 1685
  population_18_64: 5867
  population_65_plus: 4636
  median_household_income: 66480
  poverty_rate: 11.54
  homeownership_rate: 86.06
  unemployment_rate: 3.83
  median_home_value: 346800
  gini_index: 0.4721
  vacancy_rate: 37.64
  race_white: 8450
  race_black: 2326
  race_asian: 533
  race_native: 16
  hispanic: 432
  bachelors_plus: 4712
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.761
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.7416
  - to: "us/states/va/districts/house/67"
    rel: in-district
    area_weight: 0.7416
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Northumberland County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12188 |
| Under 18 | 1685 |
| 18–64 | 5867 |
| 65+ | 4636 |
| Median household income | 66480 |
| Poverty rate | 11.54 |
| Homeownership rate | 86.06 |
| Unemployment rate | 3.83 |
| Median home value | 346800 |
| Gini index | 0.4721 |
| Vacancy rate | 37.64 |
| White | 8450 |
| Black | 2326 |
| Asian | 533 |
| Native | 16 |
| Hispanic/Latino | 432 |
| Bachelor's or higher | 4712 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 76% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 74% (state senate)
- [VA House District 67](/us/states/va/districts/house/67.md) — 74% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
