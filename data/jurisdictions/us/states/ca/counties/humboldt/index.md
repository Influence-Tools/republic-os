---
type: Jurisdiction
title: "Humboldt County, CA"
classification: county
fips: "06023"
state: "CA"
demographics:
  population: 134541
  population_under_18: 25301
  population_18_64: 82580
  population_65_plus: 26660
  median_household_income: 61160
  poverty_rate: 18.67
  homeownership_rate: 56.54
  unemployment_rate: 9.02
  median_home_value: 446900
  gini_index: 0.48
  vacancy_rate: 12.66
  race_white: 97012
  race_black: 2137
  race_asian: 4137
  race_native: 5195
  hispanic: 19039
  bachelors_plus: 41875
districts:
  - to: "us/states/ca/districts/02"
    rel: in-district
    area_weight: 0.8909
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.891
  - to: "us/states/ca/districts/house/2"
    rel: in-district
    area_weight: 0.891
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Humboldt County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 134541 |
| Under 18 | 25301 |
| 18–64 | 82580 |
| 65+ | 26660 |
| Median household income | 61160 |
| Poverty rate | 18.67 |
| Homeownership rate | 56.54 |
| Unemployment rate | 9.02 |
| Median home value | 446900 |
| Gini index | 0.48 |
| Vacancy rate | 12.66 |
| White | 97012 |
| Black | 2137 |
| Asian | 4137 |
| Native | 5195 |
| Hispanic/Latino | 19039 |
| Bachelor's or higher | 41875 |

## Districts

- [CA-02](/us/states/ca/districts/02.md) — 89% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 89% (state senate)
- [CA House District 2](/us/states/ca/districts/house/2.md) — 89% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
