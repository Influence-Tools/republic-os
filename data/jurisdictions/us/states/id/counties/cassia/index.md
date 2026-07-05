---
type: Jurisdiction
title: "Cassia County, ID"
classification: county
fips: "16031"
state: "ID"
demographics:
  population: 25483
  population_under_18: 7879
  population_18_64: 13911
  population_65_plus: 3693
  median_household_income: 70830
  poverty_rate: 12.41
  homeownership_rate: 68.63
  unemployment_rate: 2.41
  median_home_value: 284600
  gini_index: 0.4423
  vacancy_rate: 6.61
  race_white: 17679
  race_black: 118
  race_asian: 67
  race_native: 456
  hispanic: 7664
  bachelors_plus: 4193
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/id/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Cassia County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25483 |
| Under 18 | 7879 |
| 18–64 | 13911 |
| 65+ | 3693 |
| Median household income | 70830 |
| Poverty rate | 12.41 |
| Homeownership rate | 68.63 |
| Unemployment rate | 2.41 |
| Median home value | 284600 |
| Gini index | 0.4423 |
| Vacancy rate | 6.61 |
| White | 17679 |
| Black | 118 |
| Asian | 67 |
| Native | 456 |
| Hispanic/Latino | 7664 |
| Bachelor's or higher | 4193 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 27](/us/states/id/districts/senate/27.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
