---
type: Jurisdiction
title: "Bingham County, ID"
classification: county
fips: "16011"
state: "ID"
demographics:
  population: 49664
  population_under_18: 14456
  population_18_64: 27670
  population_65_plus: 7538
  median_household_income: 77878
  poverty_rate: 11.71
  homeownership_rate: 80.5
  unemployment_rate: 5.44
  median_home_value: 293300
  gini_index: 0.4205
  vacancy_rate: 7.96
  race_white: 38331
  race_black: 96
  race_asian: 144
  race_native: 2598
  hispanic: 8829
  bachelors_plus: 8718
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Bingham County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49664 |
| Under 18 | 14456 |
| 18–64 | 27670 |
| 65+ | 7538 |
| Median household income | 77878 |
| Poverty rate | 11.71 |
| Homeownership rate | 80.5 |
| Unemployment rate | 5.44 |
| Median home value | 293300 |
| Gini index | 0.4205 |
| Vacancy rate | 7.96 |
| White | 38331 |
| Black | 96 |
| Asian | 144 |
| Native | 2598 |
| Hispanic/Latino | 8829 |
| Bachelor's or higher | 8718 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 30](/us/states/id/districts/senate/30.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
