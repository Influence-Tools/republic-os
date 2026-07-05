---
type: Jurisdiction
title: "Jackson County, IL"
classification: county
fips: "17077"
state: "IL"
demographics:
  population: 53064
  population_under_18: 9994
  population_18_64: 34292
  population_65_plus: 8778
  median_household_income: 48763
  poverty_rate: 20.99
  homeownership_rate: 49.98
  unemployment_rate: 7.47
  median_home_value: 137300
  gini_index: 0.4936
  vacancy_rate: 17.21
  race_white: 38642
  race_black: 7422
  race_asian: 1970
  race_native: 45
  hispanic: 2811
  bachelors_plus: 16783
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.5824
  - to: "us/states/il/districts/house/115"
    rel: in-district
    area_weight: 0.5824
  - to: "us/states/il/districts/house/118"
    rel: in-district
    area_weight: 0.4175
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Jackson County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53064 |
| Under 18 | 9994 |
| 18–64 | 34292 |
| 65+ | 8778 |
| Median household income | 48763 |
| Poverty rate | 20.99 |
| Homeownership rate | 49.98 |
| Unemployment rate | 7.47 |
| Median home value | 137300 |
| Gini index | 0.4936 |
| Vacancy rate | 17.21 |
| White | 38642 |
| Black | 7422 |
| Asian | 1970 |
| Native | 45 |
| Hispanic/Latino | 2811 |
| Bachelor's or higher | 16783 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 58% (state senate)
- [IL House District 115](/us/states/il/districts/house/115.md) — 58% (state house)
- [IL House District 118](/us/states/il/districts/house/118.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
