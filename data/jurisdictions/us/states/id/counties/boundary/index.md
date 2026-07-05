---
type: Jurisdiction
title: "Boundary County, ID"
classification: county
fips: "16021"
state: "ID"
demographics:
  population: 13172
  population_under_18: 3072
  population_18_64: 7007
  population_65_plus: 3093
  median_household_income: 67237
  poverty_rate: 13.65
  homeownership_rate: 75.29
  unemployment_rate: 2.59
  median_home_value: 410500
  gini_index: 0.4558
  vacancy_rate: 10.13
  race_white: 10918
  race_black: 43
  race_asian: 272
  race_native: 208
  hispanic: 753
  bachelors_plus: 2988
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/id/districts/senate/1"
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

# Boundary County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13172 |
| Under 18 | 3072 |
| 18–64 | 7007 |
| 65+ | 3093 |
| Median household income | 67237 |
| Poverty rate | 13.65 |
| Homeownership rate | 75.29 |
| Unemployment rate | 2.59 |
| Median home value | 410500 |
| Gini index | 0.4558 |
| Vacancy rate | 10.13 |
| White | 10918 |
| Black | 43 |
| Asian | 272 |
| Native | 208 |
| Hispanic/Latino | 753 |
| Bachelor's or higher | 2988 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 1](/us/states/id/districts/senate/1.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
