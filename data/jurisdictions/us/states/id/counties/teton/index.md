---
type: Jurisdiction
title: "Teton County, ID"
classification: county
fips: "16081"
state: "ID"
demographics:
  population: 12425
  population_under_18: 2775
  population_18_64: 7872
  population_65_plus: 1778
  median_household_income: 99805
  poverty_rate: 9.12
  homeownership_rate: 80.82
  unemployment_rate: 1.21
  median_home_value: 690500
  gini_index: 0.4229
  vacancy_rate: 27.84
  race_white: 10075
  race_black: 0
  race_asian: 10
  race_native: 97
  hispanic: 2146
  bachelors_plus: 5836
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/id/districts/senate/35"
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

# Teton County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12425 |
| Under 18 | 2775 |
| 18–64 | 7872 |
| 65+ | 1778 |
| Median household income | 99805 |
| Poverty rate | 9.12 |
| Homeownership rate | 80.82 |
| Unemployment rate | 1.21 |
| Median home value | 690500 |
| Gini index | 0.4229 |
| Vacancy rate | 27.84 |
| White | 10075 |
| Black | 0 |
| Asian | 10 |
| Native | 97 |
| Hispanic/Latino | 2146 |
| Bachelor's or higher | 5836 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 35](/us/states/id/districts/senate/35.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
