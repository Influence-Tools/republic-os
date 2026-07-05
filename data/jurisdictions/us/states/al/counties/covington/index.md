---
type: Jurisdiction
title: "Covington County, AL"
classification: county
fips: "01039"
state: "AL"
demographics:
  population: 37628
  population_under_18: 8346
  population_18_64: 20927
  population_65_plus: 8355
  median_household_income: 52456
  poverty_rate: 19.19
  homeownership_rate: 76.27
  unemployment_rate: 5.17
  median_home_value: 152100
  gini_index: 0.4876
  vacancy_rate: 21.76
  race_white: 31206
  race_black: 4497
  race_asian: 173
  race_native: 117
  hispanic: 765
  bachelors_plus: 6474
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/al/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/92"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Covington County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37628 |
| Under 18 | 8346 |
| 18–64 | 20927 |
| 65+ | 8355 |
| Median household income | 52456 |
| Poverty rate | 19.19 |
| Homeownership rate | 76.27 |
| Unemployment rate | 5.17 |
| Median home value | 152100 |
| Gini index | 0.4876 |
| Vacancy rate | 21.76 |
| White | 31206 |
| Black | 4497 |
| Asian | 173 |
| Native | 117 |
| Hispanic/Latino | 765 |
| Bachelor's or higher | 6474 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 31](/us/states/al/districts/senate/31.md) — 100% (state senate)
- [AL House District 92](/us/states/al/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
